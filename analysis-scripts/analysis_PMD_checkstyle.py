import os
import subprocess
import json
import pandas as pd
import re
from collections import defaultdict

def extract_checkstyle_issues(report_path, category_to_rules):
    """Extract and categorize Checkstyle issues from a report file."""
    categorized_issues = defaultdict(list)
    error_code_counts = defaultdict(lambda: defaultdict(int))
    
    with open(report_path, 'r') as file:
        for line in file:
            match = re.search(r"\[(\w+)]$", line)
            if match:
                rule_name = match.group(1)
                issue_detail = line.split(":")[-2].strip() + ": " + line.split(":")[-1].strip()
                for category, rules in category_to_rules.items():
                    if rule_name in rules:
                        categorized_issues[category].append(f"{issue_detail} [{rule_name}]")
                        error_code_counts[category][rule_name] += 1
                        break
    return categorized_issues, error_code_counts

def extract_pmd_violations(report_path):
    """Extract PMD violations from a report file."""
    violations = []
    violation_counts = defaultdict(int)
    with open(report_path, 'r') as file:
        for line in file:
            parts = line.split(":\t")
            if len(parts) > 1:
                category_message = parts[1].strip()
                violations.append(category_message)
                violation_counts[category_message] += 1
    return violations, violation_counts

def run_checkstyle_analysis(input_folder, checkstyle_output_dir):
    os.makedirs(checkstyle_output_dir, exist_ok=True)
    results = []
    checkstyle_issues = defaultdict(list)
    error_code_counts = defaultdict(lambda: defaultdict(int))
    checkstyle_jar = os.path.expanduser("~/checkstyle/checkstyle-10.21.1-all.jar")
    config_file = os.path.expanduser("~/checkstyle/sun_checks.xml")
    
    category_to_rules = {
        "annotation": ["AnnotationLocation", "AnnotationOnSameLine", "AnnotationUseStyle", "MissingDeprecated", "MissingOverride", "PackageAnnotation"],
        "blocks": ["AvoidNestedBlocks", "EmptyBlock", "EmptyCatchBlock", "LeftCurly", "NeedBraces", "RightCurly"],
        "coding": ["ArrayTrailingComma", "AvoidDoubleBraceInitialization", "AvoidInlineConditionals", "AvoidNoArgumentSuperConstructorCall", "ConstructorsDeclarationGrouping", "CovariantEquals", "DeclarationOrder", "DefaultComesLast", "EmptyStatement", "EqualsAvoidNull", "EqualsHashCode", "ExplicitInitialization", "FallThrough", "FinalLocalVariable", "HiddenField", "IllegalCatch", "IllegalInstantiation", "IllegalThrows", "IllegalToken", "IllegalTokenText", "IllegalType", "InnerAssignment", "MagicNumber", "MatchXpath", "MissingCtor", "MissingNullCaseInSwitch", "MissingSwitchDefault", "ModifiedControlVariable", "MultipleStringLiterals", "MultipleVariableDeclarations", "NestedForDepth", "NestedIfDepth", "NestedTryDepth", "NoArrayTrailingComma", "NoClone", "NoEnumTrailingComma", "NoFinalizer", "OneStatementPerLine", "OverloadMethodsDeclarationOrder", "PackageDeclaration", "ParameterAssignment", "RequireThis", "ReturnCount", "SimplifyBooleanExpression", "SimplifyBooleanReturn", "StringLiteralEquality", "SuperClone", "SuperFinalize", "UnnecessaryParentheses", "UnnecessarySemicolonAfterOuterTypeDeclaration", "UnnecessarySemicolonAfterTypeMemberDeclaration", "UnnecessarySemicolonInEnumeration", "UnnecessarySemicolonInTryWithResources", "UnusedCatchParameterShouldBeUnnamed", "UnusedLambdaParameterShouldBeUnnamed", "UnusedLocalVariable", "VariableDeclarationUsageDistance", "WhenShouldBeUsed"],
        "design": ["DesignForExtension", "FinalClass", "HideUtilityClassConstructor", "InnerTypeLast", "InterfaceIsType", "MutableException", "OneTopLevelClass", "SealedShouldHavePermitsList", "ThrowsCount", "VisibilityModifier"],
        "imports": ["AvoidStarImport", "AvoidStaticImport", "CustomImportOrder", "IllegalImport", "ImportControl", "ImportOrder", "RedundantImport", "UnusedImports"],
        "javadoc": ["AtclauseOrder", "InvalidJavadocPosition", "JavadocBlockTagLocation", "JavadocContentLocation", "JavadocLeadingAsteriskAlign", "JavadocMethod", "JavadocMissingLeadingAsterisk", "JavadocMissingWhitespaceAfterAsterisk", "JavadocPackage", "JavadocParagraph", "JavadocStyle", "JavadocTagContinuationIndentation", "JavadocType", "JavadocVariable", "MissingJavadocMethod", "MissingJavadocPackage", "MissingJavadocType", "NonEmptyAtclauseDescription", "RequireEmptyLineBeforeBlockTagGroup", "SingleLineJavadoc", "SummaryJavadoc", "WriteTag"],
        "metrics": ["BooleanExpressionComplexity", "ClassDataAbstractionCoupling", "ClassFanOutComplexity", "CyclomaticComplexity", "JavaNCSS", "NPathComplexity"],
        "modifiers": ["ClassMemberImpliedModifier", "InterfaceMemberImpliedModifier", "ModifierOrder", "RedundantModifier"],
        "naming": ["AbbreviationAsWordInName", "AbstractClassName", "CatchParameterName", "ClassTypeParameterName", "ConstantName", "IllegalIdentifierName", "InterfaceTypeParameterName", "LambdaParameterName", "LocalFinalVariableName", "LocalVariableName", "MemberName", "MethodName", "MethodTypeParameterName", "PackageName", "ParameterName", "PatternVariableName", "RecordComponentName", "RecordTypeParameterName", "StaticVariableName", "TypeName"],
        "regexp": ["Regexp", "RegexpMultiline", "RegexpOnFilename", "RegexpSingleline", "RegexpSinglelineJava"],
        "whitespace": ["EmptyForInitializerPad", "EmptyForIteratorPad", "EmptyLineSeparator", "FileTabCharacter", "GenericWhitespace", "MethodParamPad", "NoLineWrap", "NoWhitespaceAfter", "NoWhitespaceBefore", "NoWhitespaceBeforeCaseDefaultColon", "OperatorWrap", "ParenPad", "SeparatorWrap", "SingleSpaceSeparator", "TypecastParenPad", "WhitespaceAfter", "WhitespaceAround"]
    }
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".java"):
            file_path = os.path.join(input_folder, filename)
            task_id = filename.replace(".java", "")
            result = {"Task ID": task_id, "Generated Code": open(file_path).read()}
            output_file = os.path.join(checkstyle_output_dir, f"{task_id}_checkstyle.txt")
            with open(output_file, 'w') as output:
                subprocess.run(["java", "-jar", checkstyle_jar, "-c", config_file, file_path], stdout=output, stderr=subprocess.STDOUT)
            categorized_issues, file_error_counts = extract_checkstyle_issues(output_file, category_to_rules)
            for category, issues in categorized_issues.items():
                result[category] = "\n".join(issues)
                checkstyle_issues[category].extend(issues)
            for category, errors in file_error_counts.items():
                for rule, count in errors.items():
                    error_code_counts[category][rule] += count
            results.append(result)
    pd.DataFrame(results).to_excel(os.path.join(checkstyle_output_dir, 'checkstyle_analysis.xlsx'), index=False)
    generate_checkstyle_summary_json(checkstyle_output_dir, checkstyle_issues, error_code_counts, category_to_rules)

def generate_checkstyle_summary_json(output_dir, checkstyle_issues, error_code_counts, category_to_rules):
    total_files = len([f for f in os.listdir(output_dir) if f.endswith('_checkstyle.txt')])
    total_issues = {category: len(issues) for category, issues in checkstyle_issues.items()}
    formatted_error_counts = {category: dict(errors) for category, errors in error_code_counts.items()}
    for category in category_to_rules.keys():
        if category not in formatted_error_counts:
            formatted_error_counts[category] = {}
    summary = {
        "Total code count": {"files": total_files},
        "Total Rule Violations": total_issues,
        "Error Code Counts": formatted_error_counts
    }
    with open(os.path.join(output_dir, "checkstyle_summary.json"), 'w') as json_file:
        json.dump(summary, json_file, indent=4)

def run_pmd_analysis(input_folder, pmd_output_dir):
    os.makedirs(pmd_output_dir, exist_ok=True)
    categories = ["bestpractices", "codestyle", "design", "documentation", "errorprone", "multithreading", "performance", "security"]
    results = []
    all_counts = defaultdict(int)
    error_code_counts = defaultdict(lambda: defaultdict(int))
    processed_files = set()
    pmd_path = os.path.expanduser("~/pmd-bin-7.6.0/bin/pmd")
    for filename in os.listdir(input_folder):
        if filename.endswith(".java"):
            file_path = os.path.join(input_folder, filename)
            task_id = filename.replace(".java", "")
            processed_files.add(task_id)
            result = {"Task ID": task_id, "Generated Code": open(file_path).read()}
            for category in categories:
                output_file = os.path.join(pmd_output_dir, f"{task_id}_{category}.txt")
                subprocess.run([pmd_path, "check", "-d", file_path, "-R", f"category/java/{category}.xml", "-f", "text", "-r", output_file])
                violations, violation_counts = extract_pmd_violations(output_file)
                all_counts[category] += len(violations)
                for violation, count in violation_counts.items():
                    error_code_counts[category][violation] += count
            results.append(result)
    pd.DataFrame(results).to_excel(os.path.join(pmd_output_dir, 'pmd_analysis.xlsx'), index=False)
    generate_pmd_summary_json(pmd_output_dir, len(processed_files), all_counts, error_code_counts)

def generate_pmd_summary_json(output_dir, total_files, all_counts, error_code_counts):
    summary = {
        "Total code count": {"files": total_files},
        "Total Rule Violations": all_counts,
        "Error Code Counts": {category: dict(error_code_counts[category]) for category in all_counts}
    }
    with open(os.path.join(output_dir, "pmd_summary.json"), 'w') as json_file:
        json.dump(summary, json_file, indent=4)

if __name__ == "__main__":
    input_folder = "/path-to-java-file-directory/"
    checkstyle_output_dir = "/path/to/checkstyle-output/directory"
    pmd_output_dir = "/path/to/PMD-output/directory"
    run_checkstyle_analysis(input_folder, checkstyle_output_dir)
    run_pmd_analysis(input_folder, pmd_output_dir)

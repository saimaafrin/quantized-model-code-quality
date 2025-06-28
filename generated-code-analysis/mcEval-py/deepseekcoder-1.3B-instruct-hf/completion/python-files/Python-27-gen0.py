def preorder_traversal(inorder: str, postorder: str) -> str:
    """
    Reconstructs the binary tree from its inorder and postorder traversals and
    returns the preorder traversal as a string.

    Args:
    inorder (str): The inorder traversal of the binary tree.
    postorder (str): The postorder traversal of the binary tree.

    Returns:
    str: The preorder traversal of the binary tree.

    Example:
    >>> preorder_traversal('BADC', 'BDCA')
    'ABCD'
    >>> preorder_traversal('A', 'A')
    'A'
    """

    def helper(start, end):
        if start > end:
            return None

        node = TreeNode(postorder[self.index])
        self.index -= 1

        if start == end:
            return node

        index = self.map[node.val]

        node.right = helper(index + 1, end)
        node.left = helper(start, index - 1)
        return node

    self.index = len(postorder) - 1
    self.map = {v: i for i, v in enumerate(inorder)}
    return str(helper(0, len(inorder) - 1).val)
def test_preorder_traversal():
    # Test case 1
    inorder1 = "BADC"
    postorder1 = "BDCA"
    expected_preorder1 = "ABCD"
    assert preorder_traversal(inorder1, postorder1) == expected_preorder1
    print(f"Test case 1 passed. Preorder: {preorder_traversal(inorder1, postorder1)}")

    # Test case 2
    inorder2 = "DBGEACF"
    postorder2 = "DGEBFCA"
    expected_preorder2 = "ABDEGCF"
    assert preorder_traversal(inorder2, postorder2) == expected_preorder2
    print(f"Test case 2 passed. Preorder: {preorder_traversal(inorder2, postorder2)}")

    # Test case 3
    inorder3 = "A"
    postorder3 = "A"
    expected_preorder3 = "A"
    assert preorder_traversal(inorder3, postorder3) == expected_preorder3
    print(f"Test case 3 passed. Preorder: {preorder_traversal(inorder3, postorder3)}")

# Run the test function
test_preorder_traversal()
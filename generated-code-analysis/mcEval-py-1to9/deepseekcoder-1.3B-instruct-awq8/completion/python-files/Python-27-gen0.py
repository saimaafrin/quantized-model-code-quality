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

    def helper(in_start, in_end, post_start, post_end):
        if post_start > post_end:
            return None

        root = TreeNode(postorder[post_end])
        index = index_map[root.val]

        root.left = helper(in_start, index - 1, post_start, post_start + index - in_start - 1)
        root.right = helper(index + 1, in_end, post_start + index - in_start, post
                            start + index - in_start - 1)

        return root

    n = len(inorder)
    index_map = {val:idx for idx, val in enumerate(inorder)}

    return helper(0, n - 1, 0, n - 1)
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
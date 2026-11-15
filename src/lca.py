"""LCA - version récursive
Adaptations de l'algo avec la syntaxe Python (NULL -> None, "root->left" -> root.left)."""


def findLCA(root, p, q):
    # no root no LCA.
    if not root:
        return None

    # if either p or q is the root then root is LCA.
    if root == p or root == q:
        return root
    else:
        # get LCA of p and q in left subtree.
        l = findLCA(root.left, p, q)

        # get LCA of p and q in right subtree.
        r = findLCA(root.right, p, q)

        # if one of p or q is in leftsubtree and other is in right
        # then root it the LCA.
        if l and r:
            return root
        # else if l is not null, l is LCA.
        elif l:
            return l
        else:
            return r

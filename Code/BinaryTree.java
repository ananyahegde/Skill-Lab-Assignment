package Program11;
	class Node {
	    int data;
	    Node left, right;

	    public Node(int data) {
	        this.data = data;
	        this.left = this.right = null;
	    }
	}
	class BinaryTree {
	    Node root;

	    // Function to mirror the binary tree
	    void mirror(Node node) {
	        if (node == null) {
	            return;
	        }

	        // Swap left and right subtrees
	        Node temp = node.left;
	        node.left = node.right;
	        node.right = temp;

	        // Recursively call mirror on left and right subtrees
	        mirror(node.left);
	        mirror(node.right);
	    }

	    // Inorder traversal to print the tree
	    void inorder(Node node) {
	        if (node == null) {
	            return;
	        }
	        inorder(node.left);
	        System.out.print(node.data + " ");
	        inorder(node.right);
	    }

	    public static void main(String[] args) {
	        BinaryTree tree = new BinaryTree();
	        tree.root = new Node(1);
	        tree.root.left = new Node(2);
	        tree.root.right = new Node(3);
	        tree.root.left.left = new Node(4);
	        tree.root.left.right = new Node(5);
	        tree.root.right.left = new Node(6);
	        tree.root.right.right = new Node(7);

	        System.out.println("Inorder before mirroring:");
	        tree.inorder(tree.root);

	        tree.mirror(tree.root);

	        System.out.println("\nInorder after mirroring:");
	        tree.inorder(tree.root);
	    }
	}



{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Building a Trie in Python\n",
    "\n",
    "Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.\n",
    "\n",
    "Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:\n",
    "* A `Trie` class that contains the root node (empty string)\n",
    "* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.\n",
    "\n",
    "Give it a try by implementing the `TrieNode` and `Trie` classes below!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Represents a single node in the Trie\n",
    "class TrieNode:\n",
    "    def __init__(self):\n",
    "        self.is_word = False\n",
    "        self.children = dict()\n",
    "    \n",
    "    def insert(self, char):\n",
    "        self.children[char] = TrieNode()\n",
    "        \n",
    "## The Trie itself containing the root node and insert/find functions\n",
    "class Trie:\n",
    "    def __init__(self):\n",
    "        self.root = TrieNode()\n",
    "\n",
    "    def insert(self, word):\n",
    "        node = self.root\n",
    "        for char in word:\n",
    "            new_node = TrieNode()\n",
    "            child = node.children.get(char)\n",
    "            if not child:\n",
    "                node.children[char] = new_node\n",
    "                node = new_node\n",
    "            else:\n",
    "                node = child\n",
    "        \n",
    "        node.is_word = True\n",
    "        \n",
    "\n",
    "    def find(self, prefix):\n",
    "        node = self.root\n",
    "        for char in prefix:\n",
    "            node = node.children.get(char)\n",
    "            if node is None:\n",
    "                return None\n",
    "        \n",
    "        return node"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Finding Suffixes\n",
    "\n",
    "Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `[\"fun\", \"function\", \"factory\"]` and we ask for suffixes from the `f` node, we would expect to receive `[\"un\", \"unction\", \"actory\"]` back from `node.suffixes()`.\n",
    "\n",
    "Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "class TrieNode:\n",
    "    def __init__(self):\n",
    "        self.is_word = False\n",
    "        self.children = dict()\n",
    "    \n",
    "    def insert(self, char):\n",
    "        self.children[char] = TrieNode()\n",
    "        \n",
    "    def suffixes(self, suffix = ''):\n",
    "        ## Recursive function that collects the suffix for \n",
    "        ## all complete words below this point\n",
    "        \n",
    "        values = []\n",
    "        for key in self.children:\n",
    "            node = self.children.get(key)\n",
    "            if node.is_word:\n",
    "                values.append(suffix + key)\n",
    "            for item in node.suffixes(suffix=suffix+key):\n",
    "                values.append(item)\n",
    "     \n",
    "        return values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Testing it all out\n",
    "\n",
    "Run the following code to add some words to your trie and then use the interactive search box to see what your code returns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "MyTrie = Trie()\n",
    "wordList = [\n",
    "    \"ant\", \"anthology\", \"antagonist\", \"antonym\", \n",
    "    \"fun\", \"function\", \"factory\", \n",
    "    \"trie\", \"trigger\", \"trigonometry\", \"tripod\"\n",
    "]\n",
    "for word in wordList:\n",
    "    MyTrie.insert(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d0c01941c193478d89f97dc9548865f0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/html": [
       "<p>Failed to display Jupyter Widget of type <code>interactive</code>.</p>\n",
       "<p>\n",
       "  If you're reading this message in the Jupyter Notebook or JupyterLab Notebook, it may mean\n",
       "  that the widgets JavaScript is still loading. If this message persists, it\n",
       "  likely means that the widgets JavaScript library is either not installed or\n",
       "  not enabled. See the <a href=\"https://ipywidgets.readthedocs.io/en/stable/user_install.html\">Jupyter\n",
       "  Widgets Documentation</a> for setup instructions.\n",
       "</p>\n",
       "<p>\n",
       "  If you're reading this message in another frontend (for example, a static\n",
       "  rendering on GitHub or <a href=\"https://nbviewer.jupyter.org/\">NBViewer</a>),\n",
       "  it may mean that your frontend doesn't currently support widgets.\n",
       "</p>\n"
      ],
      "text/plain": [
       "interactive(children=(Text(value='', description='prefix'), Output()), _dom_classes=('widget-interact',))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from ipywidgets import widgets\n",
    "from IPython.display import display\n",
    "from ipywidgets import interact\n",
    "def f(prefix):\n",
    "    if prefix != '':\n",
    "        prefixNode = MyTrie.find(prefix)\n",
    "        if prefixNode:\n",
    "            print('\\n'.join(prefixNode.suffixes(suffix=prefix))) # Added the prefix so the autocomplete would show whole words\n",
    "        else:\n",
    "            print(prefix + \" not found\")\n",
    "    else:\n",
    "        print('')\n",
    "interact(f, prefix='');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  },
  "widgets": {
   "state": {},
   "version": "1.1.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

# Index Constructiono

# Run the program
* Type
```
python3 main.py --path PATH_TO_CRANFIELD_DIRECOTRY
```
* The only argument is **--path** that accepts the path to the CRANFIELD directory/folder.

## Data stuctures in-use
* Class **Index** is a user-defined class that acts as a LinkedList
* Class **Posting** inherits from class **Index** that acts as a posting list for each file
* Class **DocNode** is a user-defined class that acts a node in the **Index or Posting** lists.

**Notes:**
* Implemented posting lists as linkedlists gives us no memory wastage and easy insertioon/deletionn. Still, traversing to extract elements is expensive.


#ifndef DB_NODES
#define DB_NODES

// forward declarations
class Node;
class DB_Elements;

// includes
#include <map>
#include <vector>

using namespace std;

class DB_Nodes {

  private:
  map<int,Node*> nodesByIndex; // starts at 1
  map<int,Node*> nodesByID;
  DB_Elements* db_elements;

  public:
  DB_Nodes();
  ~DB_Nodes();
  unsigned int size();
  DB_Elements* get_db_elements();
  void set_db_elements(DB_Elements*);
  Node* add_node(int,vector<float>);
  Node* get_nodeByID(int);
  Node* get_nodeByIndex(int);

};

#endif

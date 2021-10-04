#topo_order_commits.py
import os
import sys
import zlib
import copy

from collections import deque

class CommitNode:
    def __init__(self, commit_hash):
      
        self.commit_hash = commit_hash
        self.parent = []
        self.children = []

#get git directory 
def get_git_directory():
    current_directory = os.getcwd()
    while ('/' != current_directory):
        if( os.path.exists(current_directory + "/.git")):
            going_in_git_directory = current_directory + "/.git"
            return going_in_git_directory
        else:
            if (os.path.exists(os.path.dirname(current_directory)) == False):
                exit(1)
            else:
                current_directory = os.path.dirname(current_directory)
    print("Not inside a git respository")
    exit(1)

#going into /refs/heads
def get_list_local_branches(git_dir, prefix = ''):

    branch_list= []
    contents_dir = os.listdir(git_dir)
    for content in contents_dir:
        name_path = git_dir + '/' + content
        is_file = os.path.isfile(name_path)
        if is_file == True:
            open_file = open(name_path, 'r')
            commit_line = open_file.readline().strip()
            branch_list.append([prefix + content, commit_line])
        else:
            branch_list.append(get_list_local_branches(name_path, prefix + content +'/')[0])
    return branch_list

#get list of local branch names 
def converting_to_head_to_branches(local_branch_heads):
    
    head_to_branches = {} #converting local_branch_heads to head_to_branches

    for item in local_branch_heads:
        if item[1] in head_to_branches:
            head_to_branches[item[1]].append(item[0])
        else:
            head_to_branches[item[1]] = [item[0]] 
    return head_to_branches

#build the commit graph 
def build_commit_graph(git_dir, local_branch_heads): 
    #Represents your graph
    commit_nodes = {}
    visited = set()

    stack = []
    for item in local_branch_heads:
        stack.append(item[1])


    while stack:
        commit_hash = stack[0]
        stack.remove(stack[0])

        if commit_hash in visited:
            continue

        visited.add(commit_hash)
        if commit_hash not in commit_nodes:
            new_commit_node = CommitNode(commit_hash)
            commit_nodes[commit_hash] = new_commit_node

        commit = commit_nodes[commit_hash]

        os.chdir(git_dir + '/objects')
        current_directory = os.getcwd()

        

        
        commit_file = current_directory + '/' + commit_hash[0:2] + '/' + commit_hash[2:]
        compressed_contents = open(commit_file, 'rb').read()
       
        decompressed_contents = zlib.decompress(compressed_contents).decode()  


        split_file = decompressed_contents.split()

        #multiple parents
        current_loc = 0
        for file in split_file:
            if (file == "parent"):
                commit.parent.append(split_file[current_loc + 1])
                current_loc = current_loc + 1
            else:
                current_loc = current_loc + 1

        for p in commit.parent:
            if p not in visited:
                stack.append(p)  #add hash to processing list

            if p not in commit_nodes:
                new_parent_commit_node = CommitNode(p)  #create a parent node and add it to the graph
                commit_nodes[p] = new_parent_commit_node
            
            parent_commit = commit_nodes[p]
            parent_commit.children.append(commit_hash)

    return commit_nodes

#topologically sort the commit graph 
def topological_sort(commit_nodes):
    result = [] #commits are sorted

    none = deque()

    copy_graph = copy.deepcopy(commit_nodes)  #copy graph 

    for commit_hash in copy_graph:  #when commit has no children
        if len(copy_graph[commit_hash].children) == 0:
            none.append(commit_hash)

    #loop to go through all commits
    while len(none) > 0:
        commit_hash = none.popleft()
        result.append(commit_hash)
        for parent_hash in list(copy_graph[commit_hash].parent):
            copy_graph[commit_hash].parent.remove(parent_hash)
            copy_graph[parent_hash].children.remove(commit_hash)

            if(len(copy_graph[parent_hash].children) == 0):
                none.append(parent_hash)

    if len(result) < len(commit_nodes): #check error
        raise Exception("cycle detected")
    return result

#print the sorted order 
def print_topo_ordered_commits_with_branch_names(commit_nodes, topo_ordered_commits, head_to_branches):
    jumped = False
    for i in range(len(topo_ordered_commits)):
        commit_hash = topo_ordered_commits[i]
        if jumped:
            jumped = False
            sticky_hash = ' '.join(commit_nodes[commit_hash].children)
            print(f'={sticky_hash}')
        branches = sorted(head_to_branches[commit_hash]) if commit_hash in head_to_branches else []
        print(commit_hash + (' ' + ' '.join(branches) if branches else ''))
        if i+1 < len(topo_ordered_commits) and topo_ordered_commits[i+1] not in commit_nodes[commit_hash].parent:
            jumped = True
            sticky_hash = ' '.join(commit_nodes[commit_hash].parent)
            print(f'{sticky_hash}=\n')


def topo_order_commits():
    #get git directory 
    git_dir = get_git_directory()

    #going into /refs/heads
    git_dir_refs_heads = git_dir + "/refs/heads"

    #get list of local branch names 
    local_branch_heads = get_list_local_branches(git_dir_refs_heads)

    #converting local_branch_heads to dict 
    head_to_branches = converting_to_head_to_branches(local_branch_heads)

    #build the commit graph 
    commit_nodes = build_commit_graph(git_dir, local_branch_heads)

    #topologically sort the commit graph 
    topo_ordered_commits = topological_sort(commit_nodes)

    #print the sorted order 
    print_topo_ordered_commits_with_branch_names(commit_nodes, topo_ordered_commits, head_to_branches)


if __name__ == '__main__':
    topo_order_commits()

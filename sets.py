def diff_symetric_set():
    print("Diff Symetric")
    set_uno = {1, 2, 3, 4, 5}
    set_dos = {4, 5, 6, 7, 8}
    print(set_uno ^ set_dos)
    
def diff_set():
    print("Diff")
    set_uno = {1, 2, 3, 4, 5}
    set_dos = {4, 5, 6, 7, 8}
    print(set_uno - set_dos)
    
def union_set():
    print("Union")
    set_uno = {1, 2, 3, 4, 5}
    set_dos = {4, 5, 6, 7, 8}
    print(set_uno | set_dos)

def intersect_set():
    print("Intersect")
    set_uno = {1, 2, 3, 4, 5}
    set_dos = {4, 5, 6, 7, 8}
    print(set_uno & set_dos)

def remove_duplicates():
    print("Remove duplicates")
    list_uno = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(set(list_uno))
    
def run():
    union_set()
    intersect_set()
    diff_set()
    diff_symetric_set()
    remove_duplicates()
    
        
if __name__ == '__main__':
    run()
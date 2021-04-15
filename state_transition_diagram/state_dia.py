
import pydot
import re


def process_edges(G):
    edge_links = {}
    cid = 0
    with open("rules.py") as f:
        for l in f.readlines():
            nums = re.findall('-?\d+\.?\d*',l)
            
            if(len(nums)!=0):
                # print(f"trans[{trans(nums[:-1])}] = {nums[-1]};")
                u = (nums[2])
                v = (nums[5])

                adj_states = list(map(int,nums[:2] + nums[3:5]))
                e_name = f"{u}->{v}"
                # print(u, e_name, v)
                
                if edge_links.get(e_name) :
                    edge_links[e_name].append(adj_states)
                else:
                    edge_links[e_name] = [adj_states]


                e = pydot.Edge(u, v,)

                if u!=v: G.add_edge(e)

    sep_str = "\n" + 1150 * "=" + "\n"
    print(*edge_links.items(), sep = sep_str)

def main():
    
    G = pydot.Dot( overlap=False, splines=True, label="[ self edges are ignored in order to avoid clutterness ]")

    process_edges(G)
    # G.write_png('as_graph.png') # use circlo engine 
    G.write_dot('as_dot_file.dot')

    
if __name__ == "__main__":
    main()



import pickle

with open("Aspectj2.pkl", "rb") as f:
    bug_lst = pickle.load(f)

for bug_index, bug in enumerate(bug_lst):
    print(bug.id)
    print(bug.file_lst, bug.commitId, bug.commit_timestamp)
    print([bug.summary, bug.description])
    # All functions in bug.commitId^
    for _, func in bug.project:
        print(func.function_name, func.file_name)
        print(func.words)
    
    for _, func in bug.project.get_all_bug_functions():
        print(func.function_name, func.file_name)
        print(func.words)
    break

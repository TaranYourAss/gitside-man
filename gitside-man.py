import requests
import json
import argparse
import os
import time
#--VARIABLES--
#get your key from here: https://github.com/settings/tokens
#don't need to worry about adding any permissions to it
#you only need to be authenticated to access the search endpoint
APIKEY = ""

# List of repos discovered during investigation
repos = []

#--FUNCTIONS--
def output(data, current_page):
    # Check if the current page is greater than one, if so, update index accordingly
    if current_page > 1:
        count = current_page * 100 + 1
    # But, if the current page is one, then at least 100 results
    # have been returned, just add 1
    elif current_page == 1:
        count = 100 + 1
    # Otherwise, we are at the beginning
    else:
        count = 1
    # Display information about the file where the keyword march was found
    # Show the owner and repository
    output_results = ""
    for snip in data[1]:
        output_result = "\n%s.  File: %s" % (str(count).zfill(2), snip['html_url'])
        output_result += "\n     Owner: %s" % snip['repository']['full_name']
        output_result += "\n     Repository: %s" % snip['repository']['html_url']
        output_result += "\n"
        output_results += output_result
        count += 1
    return output_results

def remove_dupes(seq):
   # Order preserving remove duplicates from list function
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

def log_repo_list():
    # Output list of discovered repos to user
    repo_results = ""
    for repo in remove_dupes(repos):
        repo_results += "\n+ https://github.com/%s" % repo
    return repo_results

def banner():
    #grab and print the banner
    # - Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'banner.txt')
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"[*] banner not found")
    except Exception as e:
        print(f"[*] An Error Occurred: {e}")

def github_search(query, headers, per_page="100", page_num="1"):
    # Github Search API endpoint for code on Github
    github_endpoint = "https://api.github.com/search/code"
    github_parameters = f'?q=\"{query}\"&per_page={per_page}&page={page_num}'
    # Make the request
    req = requests.get(github_endpoint + github_parameters, headers=headers)
    # Save the response 
    data = req.json()
    with open('C:\\Users\\tulrich\OneDrive - rSolutions\\Programming (rSolutions)\\Hacking\\git_search\\output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    # For each repo name, append it to the global repo list
    for result in data.get('items'):
        # Fetch the repo name and add it to the list of repos seen in results
        repo_name = result['repository']['full_name']
        repos.append(repo_name)
    # Return the total number of results and the items
    return data.get('total_count'), data.get('items')

def main(query):
    #https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28
    #apikey now needs to be in the header instead of the URL
    authorization = f"Bearer {APIKEY}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": authorization,
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # Page count specifies the current page of the search results
    PAGE_COUNT = 1
    
    try:
        results_log = ""
        # Perform an initial search and return up to 100 results
        count, results = github_search(query=query, headers=headers, per_page="100", page_num=str(PAGE_COUNT))
        # Remaining results are kept track of in results_count
        results_count = count
        # Place the results into a variable with the total number
        github_results = [count, results]
        # Output the results to the user
        print(output(github_results, PAGE_COUNT - 1))
        results_log += output(github_results, PAGE_COUNT - 1)
        print("====== DISCOVERED REPOS ======")
        print(log_repo_list())
        # Tell the user the total number of returned results
        print("\n[*] Found %s results on Github." % count)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    #standard issue argument collection
    parser = argparse.ArgumentParser(description='Search keywords from all public Github repositories. This script is set for Github API Version 2022-11-28')
    parser.add_argument('-q', '--query', dest="query", help='Query to use for searching through Github.')
    
    args = parser.parse_args()
    
    #some sort of query must be provided
    if not args.query:
        print('[*] No query has been provided. Please provide a query to search with by using -q OR --query')
        print('[*] Further information on Github queries can be found here:')
        print('https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#constructing-a-search-query')
        exit()
    else:
        query = args.query
    
    banner()
    #apikey can be hardcoded, or provided during execution.
    while not APIKEY:
        APIKEY = input("[*] Github API Key: ")
        if APIKEY == "exit":
            exit()
        
    main(query)

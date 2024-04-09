# gitside-man
Very simple OSINT Tool to search through all public Github repositories, enabling you to discover Github repositories that may contain confidential information.  

Make sure to get/create your API key from here:  
https://github.com/settings/tokens  
> [!TIP]  
> You do not need to add any special permissions to the API key. The Github API just requires you to authenticate to enable searching on repos.  

## Installation
Gitside-man can be installed by downloading the zip file [here](https://github.com/rsolutions-canada/gitside-man/archive/master.zip) or by cloning the repository:  

`git clone https://<github_apikey>@github.com/rsolutions-canada/gitside-man.git`  

Further information on cloning private Github repositories:  
https://stackoverflow.com/a/70320541  

Gitside-man works with [Python](http://www.python.org/download/) **3** on any platform.  

## Features
- Search Github for keywords belonging to confidential documents and discover leaks.
- [TODO] Perform checks on discovered repositories to confirm or deny that they belong to a target organization.
- [TODO] Log all results for further investigation and reporting.
  
## Usage
To perform a search on Github for an internal keyword, type:

`python3 gitside-man.py -q "<insert internal keyword OR Github query here>"`  

## Queries
Gitside-man allows you search for any simple keyword, as well as full Github queries with multiple keywords and qualifiers.  

A query can contain any combination of search qualifiers supported on GitHub. The format of the search query is:  

`SEARCH_KEYWORD_1 SEARCH_KEYWORD_N QUALIFIER_1 QUALIFIER_N`  

For example, if you wanted to search for all repositories owned by defunkt that contained the word GitHub and Octocat in the README file, you would use the following query with the search repositories endpoint:  

`GitHub Octocat in:readme user:defunkt`  

Source: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#constructing-a-search-query  

## Github API Key
You can grab/create you Personal Access Token here:  
https://github.com/settings/tokens  

Once you have your api key you can store it inside the script for ease-of-use.  
```python
APIKEY = "ghp_abc123"
```

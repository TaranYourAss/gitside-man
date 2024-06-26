```
                                                                                                             
              _/    _/                _/        _/                                                           
     _/_/_/      _/_/_/_/    _/_/_/        _/_/_/    _/_/                _/_/_/  _/_/      _/_/_/  _/_/_/    
  _/    _/  _/    _/      _/_/      _/  _/    _/  _/_/_/_/  _/_/_/_/_/  _/    _/    _/  _/    _/  _/    _/   
 _/    _/  _/    _/          _/_/  _/  _/    _/  _/                    _/    _/    _/  _/    _/  _/    _/    
  _/_/_/  _/      _/_/  _/_/_/    _/    _/_/_/    _/_/_/              _/    _/    _/    _/_/_/  _/    _/     
     _/                                                                                                      
_/_/                                                                                                         
```
Very simple OSINT Tool to search through all public Github repositories, enabling you to discover Github repositories that may contain confidential information.  

Make sure to get/create your API key from here:  
https://github.com/settings/tokens  
> [!TIP]  
> You do not need to add any special permissions to the API key. The Github API just requires you to authenticate to enable searching on repos.  

## Installation
Gitside-man can be installed by downloading the zip file [here](https://github.com/TaranYourAss/gitside-man/archive/master.zip) or by cloning the repository:  

`git clone https://github.com/TaranYourAss/gitside-man.git`    

## Features
- Search Github for keywords belonging to confidential documents and discover leaks.
- [TODO] Perform checks on discovered repositories to confirm or deny that they belong to a target organization.
- [TODO] Log all results for further investigation and reporting.
- [TODO] Ability to automatically find where the keyword matched within the found files
- [TODO] Display Description of found repositories
- [TODO] Add built-in pre-fabbed queries to look for sensitive info
         - API keys in found repos
         -   
  
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

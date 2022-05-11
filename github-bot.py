# github rest api

import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '123123123'      # use your own token

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self, name, url):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": url,
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()



k = 1
github = Github

while selection != '4':
    selection = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\n Please enter the number of process that you want to do: ')

    if(selection != 4):
        if(selection == '1'):
            username = input('username: ')
            result = github.getUser(username)
            print(f"Name: {result['name']}   Public Repositories: {result['public_repos']}   Followers:{result['followers']}")

        elif(selection == '2'):
            username = input("Username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])

        
        elif(selection == '3'):
            name = input('repository name: ')
            url = input('Please enter the homepage url of github account')
            result = github.createRepository(name,url)
            print(result) 
        
        else:
            print("Wrong Input Please Try Again")






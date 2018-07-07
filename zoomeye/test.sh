#!/bin/bash
curl -XPOST https://api.zoomeye.org/user/login -d '{ "username": "623257096@qq.com", "password": "cS10241024"  }'
#curl -X GET -i https://api.zoomeye.org/resources-info \
#    -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6IjYyMzI1NzA5NkBxcS5jb20iLCJpYXQiOjE1MzA4ODEyNjUsIm5iZiI6MTUzMDg4MTI2NSwiZXhwIjoxNTMwOTI0NDY1fQ.cr3pTpYg_DxPXjR2gAki0MYgCKsjODmlj-j9ytNRezs"
curl -X GET 'https://api.zoomeye.org/host/search?query=os:windows&page=1&facet=app,os' \
     -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6IjYyMzI1NzA5NkBxcS5jb20iLCJpYXQiOjE1MzA5MzEwNTgsIm5iZiI6MTUzMDkzMTA1OCwiZXhwIjoxNTMwOTc0MjU4fQ.3shU8usWDwMeTwoOlMg2yHCOXAj_GqkMVlroiCZXemc"

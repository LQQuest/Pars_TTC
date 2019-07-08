from random import  choice
useragent = open('txt//user-agent.txt').read().split('\n')
useragent = {'User-Agent': choice(useragent)}

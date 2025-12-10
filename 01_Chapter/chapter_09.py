#set

teama = {"sai","kiran","chebrolu","venkata"}

teamb ={"mounika","sri","lakshmi","sai"}

# union of two sets

team = teama | teamb

print(f"the total team {team}")


# intersection of two sets

team_intersection = teama & teamb

print(f"the common team members {team_intersection}")


# difference of two sets

team_difference = teama - teamb

print(f"the team members not in teamb {team_difference}")

print(f"Is 'vasu' in teama? {'vasu' in teama}")


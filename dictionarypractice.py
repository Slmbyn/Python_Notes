# where_my_things_are = {
#     'ps4': 'bedroom',
#     'ipad': 'backpack'
# }

# for thing, location in where_my_things_are.items():
#     print(f'My {thing} is kept in my {location}')

scores = [
   {
     'name': 'selam',
     'points': 325  # points the player scored
   }
]

scores.append({'name':'sam', 'points':80})

for score in scores:
    print(f"{score['name']} scored {score['points']} points")
    print(type(score['points']))

color = 'blue'
print(color.index('u'))
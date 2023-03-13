# Wyspa_Wilkow
This is a simple simulation game written using Python and PyGame.
It's goal is to simulate behaviour of wolfs and rabbits on an island.

# How it works
In this game we have 3 factors:
 - Board tiles
 - Rabbits
 - Wolfs
 
 # Board tiles
 Board tiles have two possible states:
  - grass tile
  - desert tile
They are a key factor in rabbit simulation because rabbits can feed only on the grass tiles. One a rabbit feeds on grass tile, this tile is replaced with desert tile. Desert tiles can't be fed on but have a possibility to randomly (4-10 ticks) regrow into a grass tile.

# Rabbits
Rabbits have a fat metter that drops down with every step. This forces them to constantly look for grass tiles to feed and replenish their fat. When male and female rabbits meet and their fat level allows it, they mate and create a new rabbit. Mating also decreases their fat level and because of that we implemented a fat treshold below which they cannot mate. Previously it led to multiple deaths. Speaking of death, rabbits also run away from wolfs whenever they are in range of rabbits sight. This chase often ends with rabbit dying of starvation.

# Wolfs
Similarly to rabbits, they also have a fat metter that drops with every step. Their only source of food are rabbits meaning that even if they "win" by eating all rabbits, they will eventually starve to death. Wolfs have a bigger range of sight than rabbits. Also similarly to rabbits, they can mate depending on their gender and fat level.
 
# Authors
<table>
<tr>
<td><p align="center">Adam Szałański</p></td>
<td><p align="center">Łucja Pałkus</p></td>
</tr>
<tr>
<td>
<a href="https://linkedin.com/in/adam-szalanski">
   <img src="https://media.licdn.com/dms/image/D4D03AQEQQN-CcweVoQ/profile-displayphoto-shrink_800_800/0/1675129015106?e=1683763200&v=beta&t=Js1TJsuLwZvTTGnCSXgcr014M445PwfR4sUXZrQ7fWA" alt="Adam Szałański">
  </a>
</td>
<td>
<a href="https://linkedin.com/in/lucja-palkus">
   <img src="https://media.licdn.com/dms/image/C4E03AQHiZl75qDVgAw/profile-displayphoto-shrink_800_800/0/1656453073719?e=1683763200&v=beta&t=CMzF7RO_2cQASvBa0P4qjfXH62EpZHLmnKDC6P8LDS4" alt="Łucja Pałkus">
  </a>
</td>
</tr>
<tr>
<td align="center">

[![LinkedIn][linkedin-shield]][linkedin-url-adam]

</td>
<td align="center">

[![LinkedIn][linkedin-shield]][linkedin-url-lucja]

</td>
</tr>
</table>



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url-adam]: https://linkedin.com/in/adam-szalanski
[linkedin-url-lucja]: https://www.linkedin.com/in/lucja-palkus/

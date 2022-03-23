from libqtile.config import Group

group_icons = ["1 ",
               "2 ☀",
               "3 ",
               "4 ",
               "5 ",
               "6",
               "7",
               "8",
               "9",
]


    
primary = "monadtall"
secondary = "max"

class CreateGroups:
    group_names = group_icons 

    
    def init_groups(self):
        """
        Return the groups of Qtile
        """
        #### First and last
        groups = [Group(name, layout=primary) if name == self.group_names[0]
                  else Group(name, layout=secondary)
                  if name == self.group_names[-1] else Group(name, layout=secondary)
                  for name in self.group_names]
        
        return groups

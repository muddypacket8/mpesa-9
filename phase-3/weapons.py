guns = {"desert eagle", "Astra"}
weapons = {"katana", "staff", "daggers", "crossbow"}

weapons.add("war harmer")
weapons.update(guns)
weapons.remove("katana")

for x in weapons.values():
  print(x)
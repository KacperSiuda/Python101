from nose.tools import *
from ex47.game import Room

def test_room():
	gold = Room("GoldRoom",
				"""W tym pokoju jest złoto, które możesz zabrać.
				   Na północy są drzwi.""")

	assert_equal(gold.name,"GoldRoom")
	assert_equal(gold.paths,{})


def test_room_paths():
	center = Room("Center", "Test pokoju pośrodku.")
	north = Room("North", "Test pokoju na północy.")
	south = Room("South", "Test pokoju na południu.")

	center.add_paths({'north':north,'south':south})
	assert_equal(center.go('north'),north)
	assert_equal(center.go('south'),south)

def test_map():
	start = Room("Start", "Możesz iść na zachód i w dół.")
	west = Room("Trees", "Tutaj są trzy drzewa, możesz iść na wschód.")
	down = Room("Dungeon", "Tu na dole jest ciemno, możesz iść do góry.")

	start.add_paths({'west': west,'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})

	assert_equal(start.go('west'),west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
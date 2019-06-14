class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        have_keys = list(set([0] + rooms[0]))
        visited_rooms = [0]
        
        for room_num in have_keys:
            if room_num not in visited_rooms:
                for key in rooms[room_num]:
                    if key not in have_keys:
                        have_keys += [key]
        if len(have_keys) == len(rooms):
            return True
        else:
            return False

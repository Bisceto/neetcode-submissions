class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # key observation, a car behind can never arrive before a car in front. they will only arrive together
        st = []
        cars = sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True)
        # Going from the closest car to the furthest car. So nobody can overtake this first car.
        for pos, spd in cars:
            time = (target - pos) / spd
            # Condition to check if behind car can catch up to front car before target
            if st and time <= st[-1][2]:
                continue
                # These cars will all join the fleet and just move at the fleet's pace. So we dont add anything
            else:
                st.append((pos, spd, time))
        return len(st)
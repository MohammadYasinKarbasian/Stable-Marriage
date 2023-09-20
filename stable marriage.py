class stable_matching:
    def __init__(self):
        self.state = None
        self.pairs = []
        self.boys = []
        self.girls = []
        self.phase1_ready = False
        self.phase2_ready = False
        self.unmatched_boys = []
        self.unmatched_girls = []
        self.is_girl_optimal = False

    def __str__(self):
        if self.is_girl_optimal:
            if self.phase1_ready == False:
                return "You should first call .get_boys_girls() function.\n"
            elif self.phase2_ready == False:
                return "You should call .stable_matcher(is_girl_optimal=False or True) function.\n"
            else:
                output = str()
                output += "\nIn girl optimal mode:\n"
                sorted_list = sorted(self.pairs, key=lambda x: x[1])
                output += "Matched pairs:\n"
                for pair in sorted_list:
                    output += f"girl{pair[1]} is mathced with boy{pair[0]}.\n"
                if self.state == 1:
                    output += "Unmatched girls:\n"
                    self.unmatched_girls.sort()
                    for girl in self.unmatched_girls:
                        output += f"girl{girl}\n"
                elif self.state == 2:
                    self.unmatched_boys.sort()
                    output += "Unmatched boys:\n"
                    for boy in self.unmatched_boys:
                        output += f"boy{boy}\n"
                return output
        else:
            if self.phase1_ready == False:
                return "You should first call .get_boys_girls() function.\n"
            elif self.phase2_ready == False:
                return "You should call .stable_matcher(is_girl_optimal=False or True) function.\n"
            else:
                output = str()
                output += "\nIn boy optimal mode:\n"
                sorted_list = sorted(self.pairs, key=lambda x: x[0])
                output += "Matched pairs:\n"
                for pair in sorted_list:
                    output += f"boy{pair[0]} is mathced with girl{pair[1]}.\n"
                if self.state == 1:
                    output += "Unmatched girls:\n"
                    self.unmatched_girls.sort()
                    for girl in self.unmatched_girls:
                        output += f"girl{girl}\n"
                elif self.state == 2:
                    self.unmatched_boys.sort()
                    output += "Unmatched boys:\n"
                    for boy in self.unmatched_boys:
                        output += f"boy{boy}\n"
                return output

    def get_boys_girls(self):
        boys_num = int(input("What is the number of boys? "))
        girls_num = int(input("What is the number of girls? "))
        for boy in range(boys_num):
            boy_prefences = list(
                map(
                    int,
                    input(
                        f"Type {girls_num} girls based on the preferences of the boy{boy} from left to right and separate each one with a space: "
                    ).split(),
                )
            )
            self.boys.append(boy_prefences)
        for girl in range(girls_num):
            girl_prefences = list(
                map(
                    int,
                    input(
                        f"Type {boys_num} boys based on the preferences of the girl{girl} from left to right and separate each one with a space: "
                    ).split(),
                )
            )
            self.girls.append(girl_prefences)
        if boys_num == girls_num:
            self.state = 0
        elif boys_num < girls_num:
            self.state = 1
        else:
            self.state = 2
        self.phase1_ready = True
        self.phase2_ready = False

    def find_girl_pair(self, girl):
        for pair in self.pairs:
            if pair[1] == girl:
                return pair[0]

    def find_boy_pair(self, boy):
        for pair in self.pairs:
            if pair[0] == boy:
                return pair[1]

    def stable_matcher(self, is_girl_optimal=False):
        self.is_girl_optimal = is_girl_optimal
        self.pairs = []
        self.unmatched_boys = [index for index in range(len(self.boys))]
        next_index_boys_request = [0 for _ in range(len(self.boys))]
        self.unmatched_girls = [index for index in range(len(self.girls))]
        next_index_girls_request = [0 for _ in range(len(self.girls))]
        if is_girl_optimal:
            if self.state == 0 or self.state == 2:
                while len(self.unmatched_girls):
                    current_girl = self.unmatched_girls.pop()
                    for best_boy in self.girls[current_girl][
                        next_index_girls_request[current_girl] :
                    ]:
                        next_index_girls_request[current_girl] += 1
                        if best_boy in self.unmatched_boys:
                            self.pairs.append([best_boy, current_girl])
                            self.unmatched_boys.remove(best_boy)
                            break

                        else:
                            matched_with_best_boy = self.find_boy_pair(best_boy)
                            if self.boys[best_boy].index(current_girl) < self.boys[
                                best_boy
                            ].index(matched_with_best_boy):
                                self.pairs.remove([best_boy, matched_with_best_boy])
                                self.pairs.append([best_boy, current_girl])
                                self.unmatched_girls.append(matched_with_best_boy)
                                break
                self.phase2_ready = True

            else:
                unwanted_girls = []
                while len(unwanted_girls) != len(self.girls) - len(self.boys):
                    current_girl = self.unmatched_girls.pop()

                    for best_boy in self.girls[current_girl][
                        next_index_girls_request[current_girl] :
                    ]:
                        next_index_girls_request[current_girl] += 1
                        if best_boy in self.unmatched_boys:
                            self.pairs.append([best_boy, current_girl])
                            self.unmatched_boys.remove(best_boy)
                            break

                        else:
                            matched_with_best_boy = self.find_boy_pair(best_boy)
                            if self.boys[best_boy].index(current_girl) < self.boys[
                                best_boy
                            ].index(matched_with_best_boy):
                                self.pairs.remove([best_boy, matched_with_best_boy])
                                self.pairs.append([best_boy, current_girl])
                                self.unmatched_girls.append(matched_with_best_boy)
                                break
                        if best_boy == self.girls[current_girl][-1]:
                            unwanted_girls.append(current_girl)
                self.unmatched_girls = unwanted_girls
                self.phase2_ready = True

        else:
            if self.state == 0 or self.state == 1:
                while len(self.unmatched_boys):
                    current_boy = self.unmatched_boys.pop()
                    for best_girl in self.boys[current_boy][
                        next_index_boys_request[current_boy] :
                    ]:
                        next_index_boys_request[current_boy] += 1
                        if best_girl in self.unmatched_girls:
                            self.pairs.append([current_boy, best_girl])
                            self.unmatched_girls.remove(best_girl)
                            break

                        else:
                            matched_with_best_girl = self.find_girl_pair(best_girl)
                            if self.girls[best_girl].index(current_boy) < self.girls[
                                best_girl
                            ].index(matched_with_best_girl):
                                self.pairs.remove([matched_with_best_girl, best_girl])
                                self.pairs.append([current_boy, best_girl])
                                self.unmatched_boys.append(matched_with_best_girl)
                                break
                self.phase2_ready = True

            else:
                unwanted_boys = []
                while len(unwanted_boys) != len(self.boys) - len(self.girls):
                    current_boy = self.unmatched_boys.pop()

                    for best_girl in self.boys[current_boy][
                        next_index_boys_request[current_boy] :
                    ]:
                        next_index_boys_request[current_boy] += 1
                        if best_girl in self.unmatched_girls:
                            self.pairs.append([current_boy, best_girl])
                            self.unmatched_girls.remove(best_girl)
                            break

                        else:
                            matched_with_best_girl = self.find_girl_pair(best_girl)
                            if self.girls[best_girl].index(current_boy) < self.girls[
                                best_girl
                            ].index(matched_with_best_girl):
                                self.pairs.remove([matched_with_best_girl, best_girl])
                                self.pairs.append([current_boy, best_girl])
                                self.unmatched_boys.append(matched_with_best_girl)
                                break
                        if best_girl == self.boys[current_boy][-1]:
                            unwanted_boys.append(current_boy)
                self.unmatched_boys = unwanted_boys
                self.phase2_ready = True


s1 = stable_matching()
s1.get_boys_girls()
s1.stable_matcher()
print(s1)
s1.stable_matcher(is_girl_optimal=True)
print(s1)
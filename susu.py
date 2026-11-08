# susu.py: records for a rotating savings group (susu)

MEMBERS = ["Ama", "Kofi", "Esi", "Yaw", "Abena"]
CONTRIBUTION = 50  # cedis each member pays every week


def pot_size(members, contribution):
      return len(members) * contribution


print("Members:", len(MEMBERS))
print("Pot each week: GH₵" + str(pot_size(MEMBERS, CONTRIBUTION)))

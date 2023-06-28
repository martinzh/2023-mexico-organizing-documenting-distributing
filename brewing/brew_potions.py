import brewing.potion_class
import brewing.containers
import brewing.cooking
import brewing.inspection


def make_example_potion(student_name):
    my_potion = brewing.potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=brewing.containers.old_kettle, heat_source=brewing.cooking.eternal_flame)
    # Simmer for 5 hours.
    brewing.cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    print("I am a Python Expert")
    # todo: write this function!
    
    return


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_example_potion(student_name=my_name)
    # Let Snape inspect the potion
    brewing.inspection.brewing.inspection_by_Snape(potion=my_potion, target_potion='example_potion')

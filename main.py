from production import forward_chain
from rules import TOURIST_RULES


def run_expert_system(rules, data):
    """
    Executes forward chaining on the provided data using the specified rules.

    Args:
        rules (tuple): A tuple of IF-THEN rules.
        data (tuple): A tuple of initial facts about a tourist.

    Returns:
        tuple: The updated data set after forward chaining.
    """
    final_data = forward_chain(rules, data, apply_only_one=False, verbose=True)
    return final_data


def ask_yes_no_question(question):
    """
    Asks a yes/no question and returns True or False based on user input.
    """
    answer = input(f"{question} (yes/no): ").strip().lower()
    return answer == "yes"


def ask_multiple_choice_question(question, choices):
    """
    Asks a multiple-choice question and returns the selected answer.
    """
    print(f"{question} (Choose one of the following: {', '.join(choices)})")
    answer = input("Your choice: ").strip().lower()
    return answer if answer in choices else None


def ask_open_ended_question(question):
    """
    Asks an open-ended question and returns the user response.
    """
    return input(f"{question}: ").strip().lower()


def generate_dynamic_questions_and_classify(rules):
    """
    Dynamically generates questions and classifies the tourist based on user input and forward chaining.

    Args:
        rules (tuple): A tuple of IF-THEN rules.

    Returns:
        list: List of classification results.
    """
    data = []

    # Initial round of questions
    if ask_yes_no_question("Does the tourist have blue skin?"):
        data.append('tourist has blue skin')
    else:
        skin_color = ask_multiple_choice_question("What is the tourist's skin color?", ["white", "yellow", "black"])
        if skin_color:
            data.append(f'tourist has {skin_color} skin')

    attire = ask_multiple_choice_question("What attire is the tourist wearing?",
                                          ["classic", "smart casual", "simple casual", "sport"])
    if attire:
        data.append(f'tourist dressed in {attire} attire')

    transport = ask_open_ended_question("What mode of transport does the tourist use?")
    data.append(f'tourist travels by {transport}')

    # Run forward chaining based on the initial answers
    current_facts = tuple(data)
    classifications = run_expert_system(rules, current_facts)

    # Now we ask follow-up questions based on the inferred facts
    if 'tourist is a wealthy_tourist' in classifications:
        if ask_yes_no_question("Does the tourist have an interest in business conferences?"):
            data.append('tourist has interest in business conferences')
        elif ask_yes_no_question("Does the tourist have an interest in shopping?"):
            data.append('tourist has interest in shopping')

    if 'tourist is a general_tourist' in classifications:
        if ask_yes_no_question("Is the tourist traveling with children or family?"):
            data.append('tourist with children')

        if ask_yes_no_question("Does the tourist have an interest in learning or research?"):
            data.append('tourist has interest in learning/research')

        if ask_yes_no_question("Does the tourist have an interest in national parks and natural reserves?"):
            data.append('tourist has interest in national parks and natural reserves')

    # Additional facts and updated classifications
    current_facts = tuple(data)
    print('\n\n', data)
    final_classifications = run_expert_system(rules, current_facts)

    # Filter final classifications
    final_classifications = [item for item in final_classifications if 'traveller!' in item]
    print("\nFinal Classification Results:")
    for item in final_classifications:
        print("-", item)
    return final_classifications


if __name__ == "__main__":
    print("Welcome to the Dynamic Tourist Classification System!")
    print("Answer the following questions to classify the tourist:\n")
    generate_dynamic_questions_and_classify(TOURIST_RULES)

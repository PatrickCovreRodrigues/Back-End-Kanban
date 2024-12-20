# from fast_zero.models.model import TodoState

# VALID_STATE_TRANSITIONS = {
#     TodoState.draft: [TodoState.todo],
#     TodoState.todo: [TodoState.doing, TodoState.trash],
#     TodoState.doing: [TodoState.done, TodoState.todo],
#     TodoState.done: [TodoState.trash],
#     TodoState.trash: [],
# }


# def is_valid_state_transition(current_state: TodoState, new_state: TodoState) -> bool:
#     return new_state in VALID_STATE_TRANSITIONS[current_state]

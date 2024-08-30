# tests/test_dialogicai.py
import pytest
from dialogicai.core import DialogicAI

def test_add_message_to_thread():
    dialogAI: DialogicAI = DialogicAI()
    
    u1 = {"content": "Hello, how are you?", "role": "user"}
    dialogAI.add_message(u1)

    assert len(dialogAI.thread) == 1
    assert dialogAI.thread[0].content == "Hello, how are you?"
    assert dialogAI.thread[0].role == "user"
    assert dialogAI.thread[0].metadata.branches == ["main"]

def test_add_message_with_new_branch():
    dialogAI = DialogicAI()
    
    u1 = {"content": "Hello, how are you?", "role": "user"}
    dialogAI.add_message(u1)
    
    u2 = {
        "content": "Can you tell me a joke?",
        "role": "user",
        "metadata": {"branches": ["joke"]}
    }
    dialogAI.add_message(u2)
    
    assert len(dialogAI.thread) == 2
    assert dialogAI.thread[1].content == "Can you tell me a joke?"
    assert dialogAI.thread[1].role == "user"
    assert dialogAI.thread[1].metadata.branches == ["joke"]
    
    # Check that the first message has been updated with the new branch
    assert "joke" in dialogAI.thread[0].metadata.branches

def test_thread_to_list():
    dialogAI = DialogicAI()

    u1 = {"content": "Hello, how are you?", "role": "user"}
    a1 = {"content": "I'm doing well, thank you! How can I assist you today?", "role": "assistant"}
    
    dialogAI.add_message(u1)
    dialogAI.add_message(a1)

    thread_list = dialogAI.thread_to_list()

    assert len(thread_list) == 2
    assert thread_list[0]["content"] == "Hello, how are you?"
    assert thread_list[1]["content"] == "I'm doing well, thank you! How can I assist you today?"
    
def test_change_branch_and_add_message():
    dialogAI = DialogicAI()

    u1 = {"content": "Hello, how are you?", "role": "user"}
    dialogAI.add_message(u1)
    
    u2 = {
        "content": "Can you tell me a joke?",
        "role": "user",
        "metadata": {"branches": ["joke"]}
    }
    dialogAI.add_message(u2)
    
    # Change branch to "joke" and add a message
    dialogAI.change_branch("joke")
    a2 = {"content": "Why don't scientists trust atoms? Because they make up everything!", "role": "assistant"}
    dialogAI.add_message(a2)
    
    assert dialogAI.target_branch == "joke"
    assert len(dialogAI.thread) == 3
    assert dialogAI.thread[2].content == "Why don't scientists trust atoms? Because they make up everything!"
    assert dialogAI.thread[2].metadata.branches == ["joke"]

# def test_get_last_message():
#     dialogAI = DialogicAI()

#     u1 = {"content": "Hello, how are you?", "role": "user"}
#     dialogAI.add_message(u1)
    
#     u2 = {
#         "content": "Can you tell me a joke?",
#         "role": "user",
#         "metadata": {"branches": ["joke"]}
#     }
#     dialogAI.add_message(u2)
    
#     last_message = dialogAI.get_last_message()
    
#     assert last_message.content == "Can you tell me a joke?"
#     assert last_message.metadata.branches == ["joke"]
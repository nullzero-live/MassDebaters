'''unit tests for the main debating file which generates the conversation
'''
import pytest
from unittest.mock import patch, Mock

def test_add_to_chat_history():
    chat = {'idx': [1], 'metadata': ["sample_data"]}
    
    result = add_to_chat_history(chat, idx, metadata)
    
    assert result['idx'] == [1]
    assert result['metadata'] == ["sample_data"]

class TestModelAction:
    def setup_method(self):
        self.model_action = ModelAction()

    @patch("PATH TO OPENAI")
    def test_question_generator(self, MockOpenAI):
        
        mock_llm = Mock()
        mock_llm.generate.return_value = "sample_question\nsample_question"
        MockOpenAI.return_value = mock_llm
        
        topic = "math"
        result = self.model_action.question_generator(topic)
        
        assert result == "sample_questionsample_question"


def test_results_initialization():
    data = {
        "questions": ["q1", "q2"],
        "answers": ["a1", "a2"]
    }
    
    result = Results(**data)
    
    assert result.questions == ["q1", "q2"]
    assert result.answers == ["a1", "a2"]





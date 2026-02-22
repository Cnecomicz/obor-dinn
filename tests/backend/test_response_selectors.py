from fixtures import incoherent_sentence, test_npc

from backend.response_selectors import ResponseSelector

# The Response algorithm in eight steps:
# (1) If the Sentence's coherence is lower than the Npc's min_coherence,
    # then the Response is selected from the Npc's incoherent_responses
    # where the key is the tuple for which the Npc's sentiment lies 
    # greater than or equal to the lower bound and strictly less than 
    # the upper bound. If the Sentence is sufficiently coherent, go to 
    # (2). Otherwise, go to (5).
# (2) Calculate the cosine similarity of the Sentence's ideology_vector 
    # and the Memory's ideology_vector. If either vector is 0, set the 
    # cosine similarity to 0. Set a boolean to True if the cosine 
    # similarity is greater than or equal to the Npc's 
    # ideology_consistency, and False otherwise.
# (3) Query the database for all Responses satisfying:
    # (a) The Sentence's relevance is greater than or equal to the 
        # Response's min_relevance
    # (b) The Npc's sentiment is greater than or equal to the Response's
        # min_sentiment and strictly less than the Response's 
        # max_sentiment
    # (c) The ideologically_consistent boolean matches the Response's
        # sentence_memory_alignment
    # (d) The ConversationState's current_topic is contained in the 
        # Response's current_topics
    # (e) The Sentence's speech_act matches the Response's speech_act
# (4) Calculate the cosine similarity between the Sentence's 
    # ideology_vector and each Response's ideology_vector, and select 
    # the Response with the largest value.
# (5) Check the Memory's log; if the Response selected is already 
    # present, include a prepended text chosen from the Npc's 
    # repetition_prefixes where the key is the tuple for which the Npc's
    # sentiment lies greater than or equal to the lower bound and 
    # strictly less than the upper bound.
# (6) Add the Response and optional prepended text to the Memory's log.
# (7) Update the Npc's sentiment based on the Response selected. Combine
    # the Response's sentiment_delta, the Npc's incoherence_penalty if 
    # applicable, and the Npc's repetition_penalty if applicable.
# (8) Set the ConversationState's current_topic to the Response's 
    # new_topic.

# Step 1
def test_incoherent_response(incoherent_sentence, test_npc):
    response_selector = ResponseSelector(
        npc=test_npc, sentence=incoherent_sentence
    )
    assert (
        response_selector.sentence.coherence 
        < response_selector.npc.min_coherence
    )
    assert response_selector.npc.sentiment == 0
    assert (
        response_selector.selected_response 
        in response_selector.npc.incoherent_responses[(-10,10)]
    )

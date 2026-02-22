from fixtures import test_npc

# Npcs have sentiment, a minimum coherence value, incoherent Responses,
# a strictness on ideological consistency, and a Memory class
def test_npc_attrs(test_npc):
    assert test_npc.sentiment == 0
    assert test_npc.min_coherence == 0.25
    assert test_npc.incoherent_responses == {
        (-float("inf"), -10): ["foo", "bar"],
        (-10, 10): ["alice", "bob"],
        (10, float("inf")): ["x", "y", "z"]
    }
    assert test_npc.ideology_consistency == -0.1
    assert hasattr(test_npc, "memory")


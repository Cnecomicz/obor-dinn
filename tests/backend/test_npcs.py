from backend.npcs import Npc

# Npcs have sentiment, a minimum coherence value, incoherent Responses,
# a strictness on ideological consistency, and a Memory class
def test_npc_attrs():
    npc = Npc("test")
    assert npc.sentiment == 0
    assert npc.min_coherence == 0.25
    assert npc.incoherent_responses == {
        (-float("inf"), -10): ["foo", "bar"],
        (-10, 10): ["alice", "bob"],
        (10, float("inf")): ["x", "y", "z"]
    }
    assert npc.ideology_consistency == -0.1
    assert has_attr(npc, "memory")


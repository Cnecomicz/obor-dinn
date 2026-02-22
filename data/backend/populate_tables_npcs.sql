/* NPC */

INSERT OR IGNORE INTO Npc (Name, MinCoherence, IdeologyConsistency)
VALUES ('test_npc', 0.25, -0.1);

/* Incoherent Responses */

/* (-inf, -10) */
INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -1e999, -10, 'foo'
FROM Npc n
WHERE n.Name='test_npc';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -1e999, -10, 'bar'
FROM Npc n
WHERE n.Name='test_npc';

/* (-10, 10) */
INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -10, 10, 'alice'
FROM Npc n
WHERE n.Name='test_npc';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -10, 10, 'bob'
FROM Npc n
WHERE n.Name='test_npc';

/* (10, inf) */
INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, 10, 1e999, 'x'
FROM Npc n
WHERE n.Name='test_npc';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, 10, 1e999, 'y'
FROM Npc n
WHERE n.Name='test_npc';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, 10, 1e999, 'z'
FROM Npc n
WHERE n.Name='test_npc';

/* (Coherent) Responses */

INSERT OR IGNORE INTO Response (
    NpcId, 
    Response, 
    MinRelevance, 
    MinSentiment, 
    MaxSentiment, 
    SentenceMemoryAlignment, 
    IdeologyVectorX,
    IdeologyVectorY,
    NextTopicId
)
SELECT 
    n.NpcId, 
    'MinRel = 0, -1 <= sentiment < 1, Aligned, (0, 0), TEST topic next',
    0,
    -1,
    1,
    True,
    0,
    0,
    t.TopicId
FROM Npc n, Topic t
WHERE n.Name='test_npc' AND t.name='TEST'
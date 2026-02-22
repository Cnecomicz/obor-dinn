/* NPC */

INSERT OR IGNORE INTO Npc (Name, MinCoherence, IdeologyConsistency)
VALUES ('test', 0.25, -0.1);

/* Incoherent Response */

/* (-inf, -10) */
INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -1e999, -10, 'foo'
FROM Npc n
WHERE n.Name='test';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -1e999, -10, 'bar'
FROM Npc n
WHERE n.Name='test';

/* (-10, 10) */
INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -10, 10, 'alice'
FROM Npc n
WHERE n.Name='test';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, -10, 10, 'bob'
FROM Npc n
WHERE n.Name='test';

/* (10, inf) */
INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, 10, 1e999, 'x'
FROM Npc n
WHERE n.Name='test';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, 10, 1e999, 'y'
FROM Npc n
WHERE n.Name='test';

INSERT OR IGNORE INTO IncoherentResponse (NpcId, MinSentiment, MaxSentiment, Response)
SELECT n.NpcId, 10, 1e999, 'z'
FROM Npc n
WHERE n.Name='test';
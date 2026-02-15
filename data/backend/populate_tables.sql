INSERT OR IGNORE INTO Word (Name) VALUES
('test_word'),
('subject'),
('verb'),
('object'),
('left'),
('right'),
('libertarian'),
('authoritarian'),
('yes');

INSERT OR IGNORE INTO Role (Name) VALUES
('SUBJECT'),
('VERB'),
('OBJECT'),
('ADJECTIVE'),
('ANSWER');

INSERT OR IGNORE INTO Ideology (Name) VALUES
('LEFT'),
('RIGHT'),
('LIBERTARIAN'),
('AUTHORITARIAN');

INSERT OR IGNORE INTO Topic (Name) VALUES
('TEST'),
('todo'),
('ANSWER');

/* Word to Role relationships */

-- test_word
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='test_word' AND r.Name IN ('SUBJECT', 'VERB', 'OBJECT', 'ADJECTIVE');

-- subject
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='subject' AND r.Name='SUBJECT';

-- verb
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='verb' AND r.Name='VERB';

-- object
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='object' AND r.Name='OBJECT';

-- left
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='left' AND r.Name IN ('SUBJECT','OBJECT','ADJECTIVE');

-- right
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='right' AND r.Name IN ('SUBJECT','OBJECT','ADJECTIVE');

-- libertarian
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='libertarian' AND r.Name IN ('SUBJECT','OBJECT','ADJECTIVE');

-- authoritarian
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='authoritarian' AND r.Name IN ('SUBJECT','OBJECT','ADJECTIVE');

-- yes
INSERT OR IGNORE INTO WordRole (WordId, RoleId)
SELECT w.WordId, r.RoleId FROM Word w, Role r
WHERE w.Name='yes' AND r.Name='ANSWER';

/* Word to Ideology relationships */

-- test_word
INSERT OR IGNORE INTO WordIdeology (WordId, IdeologyId, Value)
SELECT w.WordId, i.IdeologyId, 1
FROM Word w, Ideology i
WHERE w.Name='test_word' AND i.Name='LEFT';
INSERT OR IGNORE INTO WordIdeology (WordId, IdeologyId, Value)
SELECT w.WordId, i.IdeologyId, 1
FROM Word w, Ideology i
WHERE w.Name='test_word' AND i.Name='LIBERTARIAN';

-- left
INSERT OR IGNORE INTO WordIdeology (WordId, IdeologyId, Value)
SELECT w.WordId, i.IdeologyId, 1
FROM Word w, Ideology i
WHERE w.Name='left' AND i.Name='LEFT';

-- right
INSERT OR IGNORE INTO WordIdeology (WordId, IdeologyId, Value)
SELECT w.WordId, i.IdeologyId, 1
FROM Word w, Ideology i
WHERE w.Name='right' AND i.Name='RIGHT';

-- libertarian
INSERT OR IGNORE INTO WordIdeology (WordId, IdeologyId, Value)
SELECT w.WordId, i.IdeologyId, 1
FROM Word w, Ideology i
WHERE w.Name='libertarian' AND i.Name='LIBERTARIAN';

-- authoritarian
INSERT OR IGNORE INTO WordIdeology (WordId, IdeologyId, Value)
SELECT w.WordId, i.IdeologyId, 1
FROM Word w, Ideology i
WHERE w.Name='authoritarian' AND i.Name='AUTHORITARIAN';

/* Word to Topic relationships */

-- test_word
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='test_word'
AND t.Name='TEST';

-- subject
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='subject'
AND t.Name='TEST';

-- verb
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='verb'
AND t.Name='TEST';

-- object
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='object'
AND t.Name='TEST';

-- left
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='left'
AND t.Name='todo';

-- right
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='right'
AND t.Name='todo';

-- libertarian
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='libertarian'
AND t.Name='todo';

-- authoritarian
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='authoritarian'
AND t.Name='todo';

-- yes
INSERT OR IGNORE INTO WordTopic (WordId, TopicId)
SELECT w.WordId, t.TopicId
FROM Word w, Topic t
WHERE w.Name='yes'
AND t.Name='ANSWER';
DROP TABLE IF EXISTS Tagged;

CREATE TABLE IF NOT EXISTS Tagged  (
	owner VARCHAR(255) NOT NULL,
	name VARCHAR(255) NOT NULL,
	tag INT NOT NULL,
	PRIMARY KEY (owner, name, tag),
	FOREIGN KEY (owner, name) REFERENCES Repositories(owner, name) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (tag) REFERENCES Tags(id) ON DELETE CASCADE
);

INSERT INTO Tagged (owner, name, tag)
VALUES
('abargeryj', 'Overhold', 5),
('abargeryj', 'Voyatouch', 6),
('abargeryj', 'Zaam-Dox', 20),
('abon16', 'Tres-Zap', 12),
('abon16', 'Y-find', 12),
('aedgerton1n', 'Bamity', 22),
('aedgerton1n', 'Konklux', 22),
('aedgerton1n', 'Zoolab', 10),
('ahawke2o', 'Alpha', 6),
('ahawke2o', 'It', 10),
('ahawke2o', 'Lotlux', 5),
('ahawke2o', 'Zoolab', 24),
('ahutchinges29', 'Biodex', 7),
('ajakubowicz1j', 'Home Ing', 12),
('ajakubowicz1j', 'Stim', 23),
('ashelley6', 'Kanlam', 8),
('ashelley6', 'Lotstring', 1),
('astarbeckp', 'Home Ing', 12),
('astarbeckp', 'Lotstring', 20),
('avanyakin2n', 'Cardify', 7),
('avanyakin2n', 'Flexidy', 23),
('avanyakin2n', 'Tempsoft', 2),
('avonb', 'Cookley', 6),
('avonb', 'Job', 24),
('bdarlington1c', 'Quo Lux', 25),
('bdarlington1c', 'Zoolab', 10),
('bgalieroa', 'Bigtax', 23),
('bminer1z', 'Bitwolf', 6),
('bminer1z', 'Flexidy', 22),
('btidbold2l', 'Stronghold', 24),
('ccastiglione2r', 'Subin', 20),
('ckirsz1o', 'Alpha', 6),
('ckirsz1o', 'Opela', 3),
('ckirsz1o', 'Redhold', 17),
('ckirsz1o', 'Regrant', 14),
('ckirsz1o', 'Ronstring', 18),
('cmittene', 'Biodex', 26),
('cmittene', 'Flexidy', 19),
('cmittene', 'Span', 25),
('coglesbee2f', 'Bamity', 25),
('coglesbee2f', 'Redhold', 22),
('coglesbee2f', 'Zamit', 22),
('corsayw', 'Bitwolf', 6),
('corsayw', 'Opela', 22),
('corsayw', 'Veribet', 15),
('cteal2p', 'Bamity', 1),
('cteal2p', 'Holdlamis', 10),
('cteal2p', 'Mat Lam Tam', 13),
('cteal2p', 'Ronstring', 24),
('cteal2p', 'Ventosanzap', 12),
('ddonavan1x', 'Otcom', 15),
('ddonavan1x', 'Voltsillam', 25),
('dfenech0', 'Bitchip', 18),
('dfenech0', 'Cardguard', 5),
('dfenech0', 'Overhold', 8),
('dfenech0', 'Pannier', 11),
('dfenech0', 'Sonair', 6),
('dfenech0', 'Tampflex', 22),
('dgraundisson2a', 'Home Ing', 22),
('dgraundisson2a', 'Keylex', 1),
('dpartkya14', 'Stronghold', 12),
('dterry1l', 'Regrant', 6),
('dterry1l', 'Toughjoyfax', 16),
('dterry1l', 'Tres-Zap', 17),
('dwrinchh', 'Alphazap', 5),
('dwrinchh', 'Biodex', 22),
('dwrinchh', 'Bytecard', 24),
('dwrinchh', 'Transcof', 11),
('edumini2d', 'Bitchip', 22),
('ejennings26', 'Stim', 12),
('ejennings26', 'Y-Solowarm', 25),
('eknowlson1g', 'Latlux', 7),
('eknowlson1g', 'Ronstring', 27),
('erenonu', 'Latlux', 20),
('erenonu', 'Rank', 2),
('erenonu', 'Transcof', 16),
('etampion1b', 'Flowdesk', 23),
('etampion1b', 'Kanlam', 6),
('etampion1b', 'Konklux', 10),
('eyabsley12', 'Aerified', 26),
('eyabsley12', 'Transcof', 3),
('fcastellucci1f', 'Bytecard', 27),
('fcastellucci1f', 'Cardify', 2),
('fcastellucci1f', 'Cookley', 17),
('fcastellucci1f', 'Hatity', 6),
('fcastellucci1f', 'Kanlam', 25),
('fde2e', 'Veribet', 24),
('fgollin1e', 'Aerified', 16),
('fgollin1e', 'Namfix', 23),
('fhorsell15', 'Trippledex', 14),
('fhorsell15', 'Zoolab', 15),
('frobilart23', 'Kanlam', 21),
('ftaylersong', 'Tin', 11),
('ftaylersong', 'Viva', 7),
('ggaskampl', 'Prodder', 11),
('ghamper20', 'Zathin', 20),
('ghyslop1m', 'Bitchip', 2),
('gmaccaughen1s', 'Alphazap', 27),
('gmaccaughen1s', 'Stronghold', 27),
('gmidgley1a', 'Hatity', 5),
('gmidgley1a', 'Opela', 6),
('gmidgley1a', 'Prodder', 2),
('gsedgeworth2c', 'Andalax', 4),
('gsedgeworth2c', 'Latlux', 22),
('gsedgeworth2c', 'Temp', 2),
('gsedgeworth2c', 'Transcof', 7),
('gverrechia2b', 'Konklux', 2),
('hcalveley27', 'Bitwolf', 27),
('hcalveley27', 'Flowdesk', 2),
('hcalveley27', 'Namfix', 21),
('hcalveley27', 'Sub-Ex', 21),
('hcalveley27', 'Vagram', 14),
('hvoas18', 'Sonsing', 7),
('jadamef', 'Solarbreeze', 4),
('jpaulitschkex', 'Andalax', 21),
('jpaulitschkex', 'Mat Lam Tam', 17),
('jpaulitschkex', 'Stringtough', 10),
('jpaulitschkex', 'Trippledex', 9),
('jpaulitschkex', 'Y-Solowarm', 27),
('jsokale1v', 'Aerified', 14),
('jsokale1v', 'Flexidy', 13),
('jtapper2q', 'Voyatouch', 15),
('kduckels2g', 'Trippledex', 18),
('klanchbery1q', 'Biodex', 25),
('klanchbery1q', 'Zathin', 20),
('ktidboldq', 'Biodex', 8),
('ktidboldq', 'Flowdesk', 21),
('ktidboldq', 'Kanlam', 21),
('ktidboldq', 'Lotstring', 22),
('ktidboldq', 'Tampflex', 25),
('lcutridge22', 'Opela', 15),
('ldriscoll24', 'Alphazap', 2),
('ldriscoll24', 'It', 1),
('ldriscoll24', 'Ventosanzap', 26),
('lkittle4', 'Prodder', 10),
('lkittle4', 'Sonsing', 14),
('llanbertonis', 'Andalax', 25),
('llanbertonis', 'Prodder', 23),
('lmclardie13', 'Flowdesk', 4),
('lmclardie13', 'Matsoft', 17),
('lspringaten', 'Regrant', 17),
('lspringaten', 'Subin', 12),
('lwindus2j', 'Alphazap', 17),
('lwindus2j', 'Temp', 23),
('mbezzant17', 'Alpha', 26),
('mcorriso', 'Stringtough', 22),
('mgillino25', 'Hatity', 8),
('mhendrickxc', 'Cookley', 24),
('mhendrickxc', 'Matsoft', 4),
('mlaugharne9', 'Bigtax', 18),
('mlaugharne9', 'Tres-Zap', 26),
('mlumsdend', 'Tres-Zap', 3),
('mmaccomiskey11', 'Alphazap', 17),
('mmaccomiskey11', 'Flexidy', 1),
('mmaccomiskey11', 'Trippledex', 23),
('mmelland1h', 'Cardguard', 5),
('mmelland1h', 'Mat Lam Tam', 12),
('noffai', 'Fix San', 1),
('nrehme1t', 'Fixflex', 5),
('nrehme1t', 'Gembucket', 7),
('nrehme1t', 'Zontrax', 27),
('ntandy2m', 'Transcof', 27),
('oalchinr', 'Kanlam', 26),
('orzehor1d', 'Keylex', 5),
('osavine1u', 'Redhold', 25),
('phobble10', 'Alphazap', 17),
('phobble10', 'Zoolab', 24),
('pstrood1r', 'Fix San', 3),
('rgirton2', 'Bigtax', 6),
('rgirton2', 'Fixflex', 27),
('rgirton2', 'Konklab', 4),
('rgirton2', 'Rank', 21),
('rlobe2h', 'Fixflex', 20),
('rlobe2h', 'Overhold', 14),
('schicchetto1i', 'Gembucket', 15),
('schicchetto1i', 'Regrant', 3),
('shatt2k', 'Latlux', 8),
('shatt2k', 'Sub-Ex', 16),
('sjillett1p', 'Greenlam', 13),
('sjillett1p', 'Matsoft', 19),
('sjillett1p', 'Voltsillam', 27),
('smammatt28', 'Aerified', 22),
('smammatt28', 'Keylex', 22),
('smammatt28', 'Solarbreeze', 15),
('smammatt28', 'Temp', 5),
('smammatt28', 'Transcof', 12),
('sphillips7', 'Fix San', 1),
('sphillips7', 'Transcof', 18),
('tkinsleyv', 'Gembucket', 2),
('tleadsy', 'Duobam', 10),
('tleadsy', 'Mat Lam Tam', 25),
('tpriestm', 'Subin', 26),
('umcgerraghtyz', 'Bamity', 27),
('umcgerraghtyz', 'Opela', 22),
('umcgerraghtyz', 'Ventosanzap', 25),
('wobbard19', 'Aerified', 5),
('xfaraday2i', 'Cookley', 4),
('xfaraday2i', 'Fintone', 13),
('xfaraday2i', 'Sub-Ex', 3),
('xfaraday2i', 'Zoolab', 3);

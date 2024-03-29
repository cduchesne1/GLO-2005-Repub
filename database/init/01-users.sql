DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Users(
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    bio TEXT,
    website VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(255),
    PRIMARY KEY(username),
    UNIQUE KEY (email)
);

INSERT INTO Users(name, username, email, bio, website, company, location)
VALUES
    ('Devin Fenech', 'dfenech0', 'dfenech0@reverbnation.com', null, null, 'Voonix', 'Indonesia'),
    ('Mayer Stollenberg', 'mstollenberg1', 'mstollenberg1@opera.com', 'augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel', 'deviantart.com', null, null),
    ('Reg Girton', 'rgirton2', 'rgirton2@multiply.com', 'tortor duis mattis egestas metus aenean fermentum donec ut mauris', 'oracle.com', 'Tanoodle', null),
    ('Genia Heffernon', 'gheffernon3', 'gheffernon3@cnn.com', 'vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo', null, 'Fiveclub', null),
    ('Lexine Kittle', 'lkittle4', 'lkittle4@squidoo.com', 'sed justo pellentesque viverra pede ac diam cras pellentesque volutpat dui maecenas tristique est et tempus semper est', null, 'Vipe', null),
    ('Kristen Pelosi', 'kpelosi5', 'kpelosi5@fotki.com', 'ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae', 'php.net', 'Tanoodle', 'Slovenia'),
    ('Aubert Shelley', 'ashelley6', 'ashelley6@so-net.ne.jp', null, 'nationalgeographic.com', 'Linklinks', null),
    ('Shena Phillips', 'sphillips7', 'sphillips7@toplist.cz', 'congue eget semper rutrum nulla nunc purus phasellus in felis', null, 'Youspan', 'France'),
    ('Bev Keeney', 'bkeeney8', 'bkeeney8@blog.com', 'tortor risus dapibus augue vel accumsan tellus nisi eu orci mauris lacinia sapien quis libero nullam sit', null, null, null),
    ('Miranda Laugharne', 'mlaugharne9', 'mlaugharne9@oakley.com', null, null, 'Photojam', null),
    ('Barry Galiero', 'bgalieroa', 'bgalieroa@cdc.gov', null, null, null, null),
    ('Aloysius von Nassau', 'avonb', 'avonb@google.ru', 'non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut', null, 'Bluejam', null),
    ('Maressa Hendrickx', 'mhendrickxc', 'mhendrickxc@ca.gov', null, 'accuweather.com', 'Trudeo', null),
    ('Manny Lumsden', 'mlumsdend', 'mlumsdend@reddit.com', 'odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim', 'vistaprint.com', null, null),
    ('Cecilius Mitten', 'cmittene', 'cmittene@go.com', 'lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed', 'cargocollective.com', 'Skinder', 'Lithuania'),
    ('Jaquith Adame', 'jadamef', 'jadamef@arizona.edu', 'purus aliquet at feugiat non pretium quis lectus suspendisse potenti in', 'ted.com', 'Mynte', null),
    ('Forbes Taylerson', 'ftaylersong', 'ftaylersong@bandcamp.com', null, 'omniture.com', 'Tagcat', 'Philippines'),
    ('Dukie Wrinch', 'dwrinchh', 'dwrinchh@rakuten.co.jp', 'vel sem sed sagittis nam congue risus semper porta volutpat quam', null, null, 'Indonesia'),
    ('Nicola Offa', 'noffai', 'noffai@ft.com', 'sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus', null, 'Gigabox', null),
    ('Abrahan Bargery', 'abargeryj', 'abargeryj@salon.com', 'aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien sapien', 'cyberchimps.com', 'Feedfire', null),
    ('Perl Schimonek', 'pschimonekk', 'pschimonekk@utexas.edu', null, 'blinklist.com', 'Flashset', 'China'),
    ('Gino Gaskamp', 'ggaskampl', 'ggaskampl@trellian.com', 'magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis', null, null, null),
    ('Trude Priest', 'tpriestm', 'tpriestm@jugem.jp', null, 'ed.gov', 'Oodoo', 'China'),
    ('Lawry Springate', 'lspringaten', 'lspringaten@newsvine.com', 'diam vitae quam suspendisse potenti nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris', null, 'Dabshots', null),
    ('Madlin Corris', 'mcorriso', 'mcorriso@nps.gov', 'suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec ut mauris', null, 'Avamba', null),
    ('Adelina Starbeck', 'astarbeckp', 'astarbeckp@unc.edu', 'erat id mauris vulputate elementum nullam varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas', 'free.fr', null, null),
    ('Kiley Tidbold', 'ktidboldq', 'ktidboldq@chronoengine.com', 'sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede', null, 'Skiptube', null),
    ('Osbert Alchin', 'oalchinr', 'oalchinr@google.ca', null, 't.co', 'Meeveo', null),
    ('Lanna Lanbertoni', 'llanbertonis', 'llanbertonis@bravesites.com', 'ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus dolor vel est donec', 'topsy.com', null, null),
    ('Aura Labell', 'alabellt', 'alabellt@intel.com', 'et eros vestibulum ac est lacinia nisi venenatis tristique fusce', 'independent.co.uk', 'Twimm', null),
    ('Emmett Renon', 'erenonu', 'erenonu@mit.edu', 'velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum', 'freewebs.com', 'Digitube', null),
    ('Tris Kinsley', 'tkinsleyv', 'tkinsleyv@independent.co.uk', 'suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in', null, 'Skyble', null),
    ('Charmain Orsay', 'corsayw', 'corsayw@surveymonkey.com', 'luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst', null, 'Skyba', null),
    ('Jody Paulitschke', 'jpaulitschkex', 'jpaulitschkex@github.io', 'gravida sem praesent id massa id nisl venenatis lacinia aenean sit amet justo', null, 'Jayo', 'Afghanistan'),
    ('Theo Leads', 'tleadsy', 'tleadsy@baidu.com', 'ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non velit donec diam', null, 'Rhynoodle', null),
    ('Ulick McGerraghty', 'umcgerraghtyz', 'umcgerraghtyz@google.co.uk', 'lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum', 'mit.edu', null, null),
    ('Philly Hobble', 'phobble10', 'phobble10@gov.uk', 'in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo', null, null, null),
    ('Minerva MacComiskey', 'mmaccomiskey11', 'mmaccomiskey11@usatoday.com', null, null, 'Fivebridge', null),
    ('Edy Yabsley', 'eyabsley12', 'eyabsley12@amazon.co.uk', null, null, 'Jaxnation', 'Latvia'),
    ('Livvyy McLardie', 'lmclardie13', 'lmclardie13@weebly.com', null, 'dailymail.co.uk', 'Feedbug', 'Russia'),
    ('Dex Partkya', 'dpartkya14', 'dpartkya14@deliciousdays.com', 'a feugiat et eros vestibulum ac est lacinia nisi venenatis tristique fusce congue', null, 'Yamia', null),
    ('Farica Horsell', 'fhorsell15', 'fhorsell15@ustream.tv', 'eu orci mauris lacinia sapien quis libero nullam sit amet turpis', 'comsenz.com', 'Browsetype', null),
    ('Andrei Bon', 'abon16', 'abon16@harvard.edu', 'purus aliquet at feugiat non pretium quis lectus suspendisse potenti', null, null, null),
    ('Marje Bezzant', 'mbezzant17', 'mbezzant17@biglobe.ne.jp', 'elementum in hac habitasse platea dictumst morbi vestibulum velit id pretium iaculis diam erat fermentum justo', 'unc.edu', 'Shufflebeat', 'Russia'),
    ('Hill Voas', 'hvoas18', 'hvoas18@deliciousdays.com', 'lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu libero rutrum', null, 'Trupe', null),
    ('Warren Obbard', 'wobbard19', 'wobbard19@about.com', 'primis in faucibus orci luctus et ultrices posuere cubilia curae', 'rakuten.co.jp', 'Wordify', null),
    ('Gwen Midgley', 'gmidgley1a', 'gmidgley1a@army.mil', null, 'tripod.com', 'Agimba', null),
    ('Emilee Tampion', 'etampion1b', 'etampion1b@seesaa.net', null, 'wsj.com', 'Jabberbean', null),
    ('Blisse Darlington', 'bdarlington1c', 'bdarlington1c@t.co', 'purus sit amet nulla quisque arcu libero rutrum ac lobortis vel dapibus at diam nam tristique tortor eu', null, 'Dazzlesphere', null),
    ('Olenolin Rzehor', 'orzehor1d', 'orzehor1d@marriott.com', 'sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula', 'hubpages.com', 'Abata', null),
    ('Fey Gollin', 'fgollin1e', 'fgollin1e@booking.com', 'eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra', null, 'Photobug', null),
    ('Fabio Castellucci', 'fcastellucci1f', 'fcastellucci1f@bandcamp.com', null, 'yelp.com', null, 'Peru'),
    ('Ediva Knowlson', 'eknowlson1g', 'eknowlson1g@nasa.gov', 'lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet', null, 'Jayo', null),
    ('Melicent Melland', 'mmelland1h', 'mmelland1h@yolasite.com', 'vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum', null, 'Topicware', 'Cameroon'),
    ('Shaun Chicchetto', 'schicchetto1i', 'schicchetto1i@usgs.gov', null, null, 'Zoomcast', 'Armenia'),
    ('Alfie Jakubowicz', 'ajakubowicz1j', 'ajakubowicz1j@weebly.com', 'massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac', null, null, 'Ukraine'),
    ('Hatti Golling', 'hgolling1k', 'hgolling1k@cocolog-nifty.com', 'dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh', 'mlb.com', null, 'Macedonia'),
    ('Deva Terry', 'dterry1l', 'dterry1l@yahoo.com', 'feugiat et eros vestibulum ac est lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien urna', 'jalbum.net', 'Oyoloo', 'Philippines'),
    ('Giacinta Hyslop', 'ghyslop1m', 'ghyslop1m@clickbank.net', 'odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat', null, null, 'Venezuela'),
    ('Amabelle Edgerton', 'aedgerton1n', 'aedgerton1n@google.com.br', 'nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris morbi non lectus aliquam', 'ted.com', 'Bluejam', null),
    ('Carly Kirsz', 'ckirsz1o', 'ckirsz1o@elpais.com', 'vestibulum velit id pretium iaculis diam erat fermentum justo nec condimentum neque sapien', null, 'Meevee', null),
    ('Scot Jillett', 'sjillett1p', 'sjillett1p@vistaprint.com', null, 'wix.com', 'Brainlounge', 'Albania'),
    ('Karlyn Lanchbery', 'klanchbery1q', 'klanchbery1q@weather.com', 'metus aenean fermentum donec ut mauris eget massa tempor convallis nulla', null, 'Buzzdog', 'Sweden'),
    ('Pierette Strood', 'pstrood1r', 'pstrood1r@prweb.com', null, 'deliciousdays.com', null, null),
    ('Ganny MacCaughen', 'gmaccaughen1s', 'gmaccaughen1s@elpais.com', null, null, null, null),
    ('Nari Rehme', 'nrehme1t', 'nrehme1t@opensource.org', 'justo sit amet sapien dignissim vestibulum vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere', null, 'Yakitri', null),
    ('Ozzy Savine', 'osavine1u', 'osavine1u@about.me', 'hac habitasse platea dictumst morbi vestibulum velit id pretium iaculis', null, 'Yoveo', null),
    ('Jonah Sokale', 'jsokale1v', 'jsokale1v@is.gd', 'risus dapibus augue vel accumsan tellus nisi eu orci mauris', null, 'Gigashots', 'China'),
    ('Tersina Danford', 'tdanford1w', 'tdanford1w@cornell.edu', 'mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis', null, 'Ainyx', null),
    ('Derby Donavan', 'ddonavan1x', 'ddonavan1x@marketwatch.com', 'proin at turpis a pede posuere nonummy integer non velit donec diam', 'blog.com', 'Gigazoom', null),
    ('Dalila Uphill', 'duphill1y', 'duphill1y@wordpress.org', 'cubilia curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus', null, null, 'Russia'),
    ('Brad Miner', 'bminer1z', 'bminer1z@amazon.de', 'sapien a libero nam dui proin leo odio porttitor id consequat', null, 'Innotype', null),
    ('Galvin Hamper', 'ghamper20', 'ghamper20@usgs.gov', 'mus etiam vel augue vestibulum rutrum rutrum neque aenean auctor gravida', 'godaddy.com', 'Oyoba', null),
    ('Mathilde Mariyushkin', 'mmariyushkin21', 'mmariyushkin21@yandex.ru', 'vivamus vestibulum sagittis sapien cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus', 'cornell.edu', 'Leexo', null),
    ('Levon Cutridge', 'lcutridge22', 'lcutridge22@theatlantic.com', 'orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi', null, 'Fadeo', null),
    ('Francis Robilart', 'frobilart23', 'frobilart23@canalblog.com', null, null, null, 'Spain'),
    ('Lexine Driscoll', 'ldriscoll24', 'ldriscoll24@slashdot.org', 'sed accumsan felis ut at dolor quis odio consequat varius integer ac', null, 'Flipopia', null),
    ('Marietta Gillino', 'mgillino25', 'mgillino25@example.com', 'orci nullam molestie nibh in lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum', null, 'Quaxo', 'Japan'),
    ('Emmy Jennings', 'ejennings26', 'ejennings26@cafepress.com', 'pellentesque viverra pede ac diam cras pellentesque volutpat dui maecenas tristique est et', null, null, 'Portugal'),
    ('Helaine Calveley', 'hcalveley27', 'hcalveley27@army.mil', 'libero nullam sit amet turpis elementum ligula vehicula consequat morbi a ipsum integer a nibh in', null, null, null),
    ('Sawyere Mammatt', 'smammatt28', 'smammatt28@admin.ch', 'auctor gravida sem praesent id massa id nisl venenatis lacinia aenean sit amet justo morbi ut odio cras mi', null, null, 'Indonesia'),
    ('Asia Hutchinges', 'ahutchinges29', 'ahutchinges29@quantcast.com', 'orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit', 'rakuten.co.jp', 'Omba', null),
    ('Demetria Graundisson', 'dgraundisson2a', 'dgraundisson2a@elegantthemes.com', null, null, null, null),
    ('Giuseppe Verrechia', 'gverrechia2b', 'gverrechia2b@ocn.ne.jp', 'orci luctus et ultrices posuere cubilia curae duis faucibus accumsan odio curabitur convallis duis consequat dui nec nisi volutpat eleifend', 'themeforest.net', 'Edgewire', null),
    ('Glenden Sedgeworth', 'gsedgeworth2c', 'gsedgeworth2c@sina.com.cn', null, 'ted.com', null, 'Ireland'),
    ('Elmo Dumini', 'edumini2d', 'edumini2d@youtube.com', 'turpis enim blandit mi in porttitor pede justo eu massa donec dapibus duis', null, 'Eamia', null),
    ('Flss de Savery', 'fde2e', 'fde2e@cmu.edu', 'in ante vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae duis faucibus', 'imgur.com', 'Skippad', null),
    ('Carmelia Oglesbee', 'coglesbee2f', 'coglesbee2f@google.es', null, 'phoca.cz', 'Livetube', null),
    ('Kristian Duckels', 'kduckels2g', 'kduckels2g@instagram.com', 'dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh fusce', 'loc.gov', null, 'Portugal'),
    ('Randal Lobe', 'rlobe2h', 'rlobe2h@i2i.jp', 'nisi eu orci mauris lacinia sapien quis libero nullam sit amet turpis elementum ligula vehicula', 'bravesites.com', 'Vipe', null),
    ('Xena Faraday', 'xfaraday2i', 'xfaraday2i@quantcast.com', 'donec dapibus duis at velit eu est congue elementum in hac', 'huffingtonpost.com', 'Twitterlist', null),
    ('Leticia Windus', 'lwindus2j', 'lwindus2j@mit.edu', 'lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue', null, 'Tagcat', null),
    ('Sunshine Hatt', 'shatt2k', 'shatt2k@unesco.org', 'odio condimentum id luctus nec molestie sed justo pellentesque viverra pede ac diam cras pellentesque', 'fc2.com', 'Yotz', null),
    ('Binky Tidbold', 'btidbold2l', 'btidbold2l@archive.org', null, null, null, null),
    ('Neale Tandy', 'ntandy2m', 'ntandy2m@unc.edu', 'sed vestibulum sit amet cursus id turpis integer aliquet massa id lobortis convallis tortor risus dapibus', null, 'Reallinks', 'Norway'),
    ('Alford Vanyakin', 'avanyakin2n', 'avanyakin2n@ifeng.com', 'nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris morbi', null, 'Devshare', 'Mexico'),
    ('Ardelis Hawke', 'ahawke2o', 'ahawke2o@quantcast.com', null, 'tamu.edu', null, null),
    ('Cass Teal', 'cteal2p', 'cteal2p@1und1.de', 'elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus', null, 'Dablist', null),
    ('Janice Tapper', 'jtapper2q', 'jtapper2q@devhub.com', 'porttitor id consequat in consequat ut nulla sed accumsan felis ut', null, null, null),
    ('Corene Castiglione', 'ccastiglione2r', 'ccastiglione2r@china.com.cn', null, 'unesco.org', 'Avaveo', 'Argentina');
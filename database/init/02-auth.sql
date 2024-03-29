DROP TABLE IF EXISTS Authentication;

CREATE TABLE IF NOT EXISTS Authentication(
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY(email),
    FOREIGN KEY(email) REFERENCES Users(email) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Authentication(email, password)
VALUES
('abargeryj@salon.com', '$2b$12$5p0PaWOkH1e1Qd2l77ocfebowFsLXURkwt0zv8M.e.Yvf8aC3Vsdi'),
('abon16@harvard.edu', '$2b$12$lk7Q.k4wS5TdcdEPu37rEOE1Gps1mul.Zygqt2RnDFRIbj2ysdG/a'),
('aedgerton1n@google.com.br', '$2b$12$VRvse6kdJot9dhiwFpk4VeVBb8wfGasjui31jVvc3Had0KBO4LuSy'),
('ahawke2o@quantcast.com', '$2b$12$lFownboEdCWrwRszUaWOG.CPAl1B1IFxO/q9LxlS6wDGfN.PsN2/u'),
('ahutchinges29@quantcast.com', '$2b$12$yJ7ctkuvJ.u1Fc/89cfgmOJLLUrRCW2m5XeOuYeGeL.Ax134B.CYu'),
('ajakubowicz1j@weebly.com', '$2b$12$a/SUlyHMuKL8pURJkC9QW.GGychaP/zanFOA150J0UTRv8f9863s2'),
('alabellt@intel.com', '$2b$12$Evd/tVh.H8dtPvNIVoLipegAY2kpSnBTohh4kI0E/ZiMY214RcbRm'),
('ashelley6@so-net.ne.jp', '$2b$12$hpcxL94/z2O7fARfpjd/Yen4j8UrfV2f2IQqtFcpdhwIVk09qhSa6'),
('astarbeckp@unc.edu', '$2b$12$zSn9Avfbak0kDDafNHc7iOAoEs8cmRlPo2ijmTDrSipADgbP.b5fy'),
('avanyakin2n@ifeng.com', '$2b$12$JCvt4vJ95Ybwq1zwpd3wteDfS2Q15DAqybc1KecZ4TR3ep4fz74nu'),
('avonb@google.ru', '$2b$12$Y4Fe0r/DIMa2sxXYwSPN1uGiddRpKRvLY6x01AsVaB5v53Axi826a'),
('bdarlington1c@t.co', '$2b$12$EeY6LGPFi7GCtHCoXv2zYO9PGA.sXjFikhrOzmjSjS9WQofRilH/y'),
('bgalieroa@cdc.gov', '$2b$12$4APHlXzoqIcF0CAZOQAswOSD1nFs7Xgma7Z5gCkUx9Vq65eo2SlUS'),
('bkeeney8@blog.com', '$2b$12$dXJw5su0e.nhGC8voWWABuvmrs232SQLpcdhX6mf8RtTqCZAoydmG'),
('bminer1z@amazon.de', '$2b$12$ovjT78VAHH4f.fQGqutktuqIkec3ZkLAeALRRJPkBd3AdITtc1tIK'),
('btidbold2l@archive.org', '$2b$12$/zvC72yLthmeDNKUOVMA0ueke2hkCBslHZHlwUpcnrKUx1iwVeClm'),
('ccastiglione2r@china.com.cn', '$2b$12$sA//Wrz27cePxiXJ2FsaU.Y4TDqPx.kU4iq4NKCyDlRHNMPWinPfG'),
('ckirsz1o@elpais.com', '$2b$12$F373v8HAVfQJ.vrAu5jPs.bfToTotCrWE1NzHi9.wYlWhWT5/VuIq'),
('cmittene@go.com', '$2b$12$hkKNN2Oho8ZIfJ44cH0AE.Smh7leP5nJe/yurOCTrceBnhG0K1KyK'),
('coglesbee2f@google.es', '$2b$12$/XmyEQ4D/.E0cIdaxgSJye05bHhZv1h5k2FJ45cfZRcJe2jDvMvaC'),
('corsayw@surveymonkey.com', '$2b$12$iexotzvdGy719PbXMhPqPugHe5o0f3gIBZ/WOXcdZ.VhbdNQxi9Ae'),
('cteal2p@1und1.de', '$2b$12$pwer2N1Syhdy.N1EsnRH..wybDMFKy6pdVnv/Mfbj1.dDpxgnbC1m'),
('ddonavan1x@marketwatch.com', '$2b$12$cnrc3KOoQjzMog0ipEZE9uybft.TkI1BOYWvcU89GX.uvU.nCZDkO'),
('dfenech0@reverbnation.com', '$2b$12$Bmc27HczZKKXUv8ZudgYFeGWIJLgpgMemmqC7wZmZwQYmGuQ8P8ku'),
('dgraundisson2a@elegantthemes.com', '$2b$12$TCdA943y7ehTlT3GahqaDuVYB0C92y5IlYUum3BYFy4bvZOsHJlB6'),
('dpartkya14@deliciousdays.com', '$2b$12$KwCvh5eczxuvyWS//Fz4MeVwQj7m57atiQBfIQW/QCcotjo2PTSyG'),
('dterry1l@yahoo.com', '$2b$12$L0mi6aSoVXzPuolOREmkbOyMGi.f0IjJPmq5ycgVG.opmOk39koyq'),
('duphill1y@wordpress.org', '$2b$12$lXgoCCalasFqglC0YSWzcuaLkmdWp1/xqCtiQjJmIa0BUCKWgV3Vi'),
('dwrinchh@rakuten.co.jp', '$2b$12$KSvP802Thf5EVdCZprccIucZFlHIx7X1nLC6J9xrrq6DyHrn65Hf6'),
('edumini2d@youtube.com', '$2b$12$8kqAV0N5Na6dSSA4LzjCaesirIPQXMPG4ab5leg.AXI7vLU/rvdpa'),
('ejennings26@cafepress.com', '$2b$12$eHSb9zjsG1ygoy83F0fHpeLywWeT1AymZpKLamnhKtX09Odtmdnsa'),
('eknowlson1g@nasa.gov', '$2b$12$vfmZdIe6WbraxHcvgb9VtuaKLSkKBrFhbaG5/6KkIR0qPyzG/1bDe'),
('erenonu@mit.edu', '$2b$12$UFgUTCbT8TKeVLHN7nnCm.7XF2R6SxjNyXZ/tZI7dHuYNqxDLld1e'),
('etampion1b@seesaa.net', '$2b$12$22KeGa8PeZ/WOo4tpDX3/eZxabtYCWbyEm5blK5Nw9yPKNzSRoblO'),
('eyabsley12@amazon.co.uk', '$2b$12$8nv9O55GwUJDc7eVfNw5SeAxDYC593qRS4lHr/5JEV8C217bbbEoe'),
('fcastellucci1f@bandcamp.com', '$2b$12$vW/Xc53aeqeMSkD5o0mxY.pYrI3C7ufDWc8fbYYKGs84bkg8gZcTq'),
('fde2e@cmu.edu', '$2b$12$UCegjjdNZ8hL9TkqFAG1qed5Q662.1fGaah9rSnSWa83kwkP1cRTq'),
('fgollin1e@booking.com', '$2b$12$kYUfAS/Pc.haIukQQi6sMOpCF1kCeJ8axJCi0T0J1kUaAyydlXggu'),
('fhorsell15@ustream.tv', '$2b$12$rnGmddoeqmAk.VI5GrrX7epklxdFuU1enttmu0BkmhbYtRxzBaPPG'),
('frobilart23@canalblog.com', '$2b$12$/IVGxOMvEZKxsaR/9H9nuOEQkhIrC2/rMJmcVbjeozaOpOkq1g2Wu'),
('ftaylersong@bandcamp.com', '$2b$12$VP.Xkhfdwg.PVe6cI5CZHuVa1CUFUpSuGHSa7sjUOjPzZX8oo7Bge'),
('ggaskampl@trellian.com', '$2b$12$1Wep9O41CPs/HeDlpJrSH.MEheOvDLPM4eDUtj54ZIBPB07LcZ8vi'),
('ghamper20@usgs.gov', '$2b$12$ssVjHuem3Besu9s1FbLgNO9KiDjqziD/cNjCHXouilZodt5oxn.BO'),
('gheffernon3@cnn.com', '$2b$12$ni90idvv7vIYQt4YPr633uUnRUHubfLrZ6vnb5ll/lv9yf.jOvDua'),
('ghyslop1m@clickbank.net', '$2b$12$GsZtbxtHeEIqi69PsDGZNuYWrFCyEtT80pbGOfyVO1xltOhwiOjYa'),
('gmaccaughen1s@elpais.com', '$2b$12$h7ciVM9pywARqWNspYyf/OCD1jsc7UpYWwwHWL3.4yL7Iz5lwQMYS'),
('gmidgley1a@army.mil', '$2b$12$2HkkVtsYHVAPwyUMWK12R.6kTExcoZA5fGRAzCJimX4c.xpfw1ncy'),
('gsedgeworth2c@sina.com.cn', '$2b$12$hOcNew1DwWEEg6/gRjcTG.naUa.pmXxdRFj4Q.jNJ8C8max3XEcje'),
('gverrechia2b@ocn.ne.jp', '$2b$12$Y0B4jMNc93EJrIECap/JCeeVN8pBlqRu3B503gM3Osdk2syOsOTSO'),
('hcalveley27@army.mil', '$2b$12$ybu92go8Lq5QTF2xIVLaGODUzKYgHN2k3zJk8LnAMswOqd12skWya'),
('hgolling1k@cocolog-nifty.com', '$2b$12$C/cbee6u9XbyFsa3POWA1Ob.XCO2.slRoEARxx3TjiUfP/zkwXIo2'),
('hvoas18@deliciousdays.com', '$2b$12$XW8ZQKljV2oH6n0PNb5SH.iUGdaUtQH7QDr9F0hC.QFMef7JvwE82'),
('jadamef@arizona.edu', '$2b$12$NAzyxSAusG21CQ3eCDpw0uHytt1E5XfoHgJi4.FZFP2qNedVkQV5.'),
('jpaulitschkex@github.io', '$2b$12$jBovZxbk5Ag38TBK6cA/AOvatKWUC5CkkoHe46Llra.dRiMyBhOT6'),
('jsokale1v@is.gd', '$2b$12$adyNMP3m1/LC5j/BrSJJROIVsCvD8UZ9nWO0qt7zsROCFV4yPlKMe'),
('jtapper2q@devhub.com', '$2b$12$me5QeTbHW5ljyqMPz71TrOayo7gprl8ZWyuCb4AyKxUjlpk6NTpqy'),
('kduckels2g@instagram.com', '$2b$12$DMlZgpoFvI4xdGzDTWJoDumNdgqm53qo9.pfUzIxegKtyi5KK6uxC'),
('klanchbery1q@weather.com', '$2b$12$1/8du7hzNfR/GY4d75MRYeCxK4hQBf5JGPN5md4wFEQ4m0eM25coa'),
('kpelosi5@fotki.com', '$2b$12$k0mKI0ULeRIER3bXAdq5YOu.nfwsqdM5yh8.WeMMn69WEdMvUDuCK'),
('ktidboldq@chronoengine.com', '$2b$12$QKfJRplj6atHXVK/MAAgO.Jif.U14vW3eVNpSX4j9cRTpm364XI4i'),
('lcutridge22@theatlantic.com', '$2b$12$IuwpOBKi7tf7KkLSsYdvMOrhwuIHLnTeVyA0eNdVCUCyzS/pkG.lu'),
('ldriscoll24@slashdot.org', '$2b$12$KE1UTk8MMPFDb3roMrr2v.M72DSXolVEEa0UzxsUZVCuCMacTgDHS'),
('lkittle4@squidoo.com', '$2b$12$xXH/yxISn5RT1kDasFb/UO./x7HtUMzVy5eYBjWvE0baP3lk4FJ0e'),
('llanbertonis@bravesites.com', '$2b$12$mquSXXDKlLRtwjB96urFseDxRPGHXf6CusH.R6BeTRXWlkYceJTPK'),
('lmclardie13@weebly.com', '$2b$12$IMxNdybMHhRtZenp7n6m8uCOwyFL/jYfzG28IlLUVhSCxC3Q75K8i'),
('lspringaten@newsvine.com', '$2b$12$gZxpmxALrP5tr0NOSaU.COFwb8n30Mn0Q4Fc/E0T9OePNN6NiXLfO'),
('lwindus2j@mit.edu', '$2b$12$WcITtkVXJ0rJe.2NgmC3KOx63UIXVVhAKnhCPegQbCIf2BbNSLove'),
('mbezzant17@biglobe.ne.jp', '$2b$12$pje24mW4XdgmuIjkPjj1VOmlFCGJ6PwNxknMWjqdQzZkA6AMHL45.'),
('mcorriso@nps.gov', '$2b$12$LFryLmDv.KN1.7JDbSPa3OqekxZnVpO1IfZgOWHM3n1oxypG/S2jK'),
('mgillino25@example.com', '$2b$12$cHMJaUEMQGAh55Jvn9JsCuG/Rqw5sgTfZcjIRpy8iTB4FZjY0Vyx.'),
('mhendrickxc@ca.gov', '$2b$12$iWrPRC8eETlPrtqTK1d1feheYOg2RwHRgHf2o/DehSzmYtGy3i4Ye'),
('mlaugharne9@oakley.com', '$2b$12$DsPMrShwo4Htni5Lok0GmOKwtUW0v8CYntWB2wiEc3/jKD0GYVitO'),
('mlumsdend@reddit.com', '$2b$12$UDDjkg30rZE99OGTQ8PBg.xaJIBvPCIKoOlpHfiT3i8vgUpTt2ZAi'),
('mmaccomiskey11@usatoday.com', '$2b$12$/wlGW7JoT1NpsUx9R1DuSuIh8B4AjwSEebgb3JBq7.5OIjQkrOEhi'),
('mmariyushkin21@yandex.ru', '$2b$12$qSvBzY74jMwQu2Hg8AVW0eLNQeoCP3g7AnfwKlZ9r4cZxWpC/dUy2'),
('mmelland1h@yolasite.com', '$2b$12$6WAF45HiNPBD4j1CsOrHdu6tcEcjaKrAcYq/SI9vIRCXK1idZbjiC'),
('mstollenberg1@opera.com', '$2b$12$PydBnndYx1kKfWMY3RTcZeG6hzlkD6inXMWj9MHI3yyBZ5YkzaO0i'),
('noffai@ft.com', '$2b$12$lGIPnjVDSFTPy/8y1.Dt9eiFjPwqb/QES6Wr7L.nHn0dnYpmCYHRC'),
('nrehme1t@opensource.org', '$2b$12$vxaJ5tHx7N0gkcR9InhoaeupqGbWKQ8PZpLoLgiRf.iEnMqV9nbNq'),
('ntandy2m@unc.edu', '$2b$12$STVsanDDAKO/iK6FW9ZYuedb8K9RMXzlhGqeMSY9AixTqnJQkjue2'),
('oalchinr@google.ca', '$2b$12$Hz7XmG/TRPKOcu7VmYd0H.pKenDarEm5fGvoNwHFT6KGW1rMwcN6W'),
('orzehor1d@marriott.com', '$2b$12$9PhKXSjxDJmyPOIs/z489O63mliGil3u1nY6FNTBLkn3dNXno1HAq'),
('osavine1u@about.me', '$2b$12$7agpdXyZUi//K8JBx0vLw.tsooleKpsUXqPaYEvJ5CpiOxXHeu3A2'),
('phobble10@gov.uk', '$2b$12$9sRwEmDwbz3QEfxsh9Da7uQ3wvVS6LPBMiqciJYS5MUg5H/J.XQR2'),
('pschimonekk@utexas.edu', '$2b$12$kkf1tyBerxbAjkU.RCycpu0WXVqYNXbyHrwEIATyTwHRJefzEinLW'),
('pstrood1r@prweb.com', '$2b$12$p/kdX8ot212AEodhilmwN.YxfWBSOB88xQayCTMTWhEUc3Y9Ycu16'),
('rgirton2@multiply.com', '$2b$12$PLim5XYkHv5.gbx7.fllku67nchoN/.8g8ekeQRL2u.TwtIQcqv5u'),
('rlobe2h@i2i.jp', '$2b$12$0CkjFs7Hy06NyApFvPf/9.2DqbmEtpQsUbbHXGEk0aRJVAWjem0uS'),
('schicchetto1i@usgs.gov', '$2b$12$/ES5scALsx3y3YcJ0uLDYOKIABfB5EG54vnpZwDHNrbmYbfevKZEO'),
('shatt2k@unesco.org', '$2b$12$1zDzAAAs7joz7jbXpq9x8uLL1xfAm4R8wbMzKHV7GGZwNTx59YHc.'),
('sjillett1p@vistaprint.com', '$2b$12$ylWpy6v8R2dNK.hXG3zkcOW8iY.OfnOU1YkhEy0abkxEaIIXrxXwa'),
('smammatt28@admin.ch', '$2b$12$vk25npw9WNKPmEZxv0pIYuqh2RdZkbBVHj.z0OpjnALS7XG7CTyzm'),
('sphillips7@toplist.cz', '$2b$12$KNDcF8kXWO8sS7QKq2xCyOHccXiyZBWrbYZaI8JQ/BRZNlci7ceEe'),
('tdanford1w@cornell.edu', '$2b$12$WFN9oL0qLBujz.05fF6CUe1xZ7IhajuEiXoFpHVIc7u.WN8zVyFSW'),
('tkinsleyv@independent.co.uk', '$2b$12$Uvvznrqx0V7QFPFuXuD..e.u62PWUIcwcF3GkZBD2LK/xNAfaUz2W'),
('tleadsy@baidu.com', '$2b$12$0FzQdfoFrGmT8VSTH9FVRuTy70tXmz4oDENoWyIz89IGXUVdqhMjq'),
('tpriestm@jugem.jp', '$2b$12$DL6Hyhi.2H9kq9fia7X8IuEeVtwjZt4u2UbrbT2uWrcpbf2XvKMua'),
('umcgerraghtyz@google.co.uk', '$2b$12$ZUy9IkefG0HDcFeJDlM8JuI4JPtYtkkY2NTAROOy6qUOY9qZYn5lC'),
('wobbard19@about.com', '$2b$12$9gFtvvCxbx8zM4TfBTLVl.tBRlbo6WSLLeWNR.exm7xgSAbvQO/Au'),
('xfaraday2i@quantcast.com', '$2b$12$aqFyws0fKO5UH4nt37q9RecRnW.1ibVvWl45/IAXLZP2Yz0c6.X72');
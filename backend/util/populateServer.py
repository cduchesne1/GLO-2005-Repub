import os

import docker
from dotenv import load_dotenv

load_dotenv()
client = docker.from_env()

repositories = [
    {
        "username": "abargeryj",
        "repository": "Overhold"
    },
    {
        "username": "abargeryj",
        "repository": "Voyatouch"
    },
    {
        "username": "abargeryj",
        "repository": "Zaam-Dox"
    },
    {
        "username": "abon16",
        "repository": "Tres-Zap"
    },
    {
        "username": "abon16",
        "repository": "Y-find"
    },
    {
        "username": "aedgerton1n",
        "repository": "Bamity"
    },
    {
        "username": "aedgerton1n",
        "repository": "Konklux"
    },
    {
        "username": "aedgerton1n",
        "repository": "Zoolab"
    },
    {
        "username": "ahawke2o",
        "repository": "Alpha"
    },
    {
        "username": "ahawke2o",
        "repository": "It"
    },
    {
        "username": "ahawke2o",
        "repository": "Lotlux"
    },
    {
        "username": "ahawke2o",
        "repository": "Zoolab"
    },
    {
        "username": "ahutchinges29",
        "repository": "Biodex"
    },
    {
        "username": "ajakubowicz1j",
        "repository": "Home Ing"
    },
    {
        "username": "ajakubowicz1j",
        "repository": "Stim"
    },
    {
        "username": "ashelley6",
        "repository": "Kanlam"
    },
    {
        "username": "ashelley6",
        "repository": "Lotstring"
    },
    {
        "username": "astarbeckp",
        "repository": "Home Ing"
    },
    {
        "username": "astarbeckp",
        "repository": "Lotstring"
    },
    {
        "username": "avanyakin2n",
        "repository": "Cardify"
    },
    {
        "username": "avanyakin2n",
        "repository": "Flexidy"
    },
    {
        "username": "avanyakin2n",
        "repository": "Tempsoft"
    },
    {
        "username": "avonb",
        "repository": "Cookley"
    },
    {
        "username": "avonb",
        "repository": "Job"
    },
    {
        "username": "bdarlington1c",
        "repository": "Quo Lux"
    },
    {
        "username": "bdarlington1c",
        "repository": "Zoolab"
    },
    {
        "username": "bgalieroa",
        "repository": "Bigtax"
    },
    {
        "username": "bminer1z",
        "repository": "Bitwolf"
    },
    {
        "username": "bminer1z",
        "repository": "Flexidy"
    },
    {
        "username": "btidbold2l",
        "repository": "Stronghold"
    },
    {
        "username": "ccastiglione2r",
        "repository": "Subin"
    },
    {
        "username": "ckirsz1o",
        "repository": "Alpha"
    },
    {
        "username": "ckirsz1o",
        "repository": "Opela"
    },
    {
        "username": "ckirsz1o",
        "repository": "Redhold"
    },
    {
        "username": "ckirsz1o",
        "repository": "Regrant"
    },
    {
        "username": "ckirsz1o",
        "repository": "Ronstring"
    },
    {
        "username": "cmittene",
        "repository": "Biodex"
    },
    {
        "username": "cmittene",
        "repository": "Flexidy"
    },
    {
        "username": "cmittene",
        "repository": "Span"
    },
    {
        "username": "coglesbee2f",
        "repository": "Bamity"
    },
    {
        "username": "coglesbee2f",
        "repository": "Redhold"
    },
    {
        "username": "coglesbee2f",
        "repository": "Zamit"
    },
    {
        "username": "corsayw",
        "repository": "Bitwolf"
    },
    {
        "username": "corsayw",
        "repository": "Opela"
    },
    {
        "username": "corsayw",
        "repository": "Veribet"
    },
    {
        "username": "cteal2p",
        "repository": "Bamity"
    },
    {
        "username": "cteal2p",
        "repository": "Holdlamis"
    },
    {
        "username": "cteal2p",
        "repository": "Mat Lam Tam"
    },
    {
        "username": "cteal2p",
        "repository": "Ronstring"
    },
    {
        "username": "cteal2p",
        "repository": "Ventosanzap"
    },
    {
        "username": "ddonavan1x",
        "repository": "Otcom"
    },
    {
        "username": "ddonavan1x",
        "repository": "Voltsillam"
    },
    {
        "username": "dfenech0",
        "repository": "Bitchip"
    },
    {
        "username": "dfenech0",
        "repository": "Cardguard"
    },
    {
        "username": "dfenech0",
        "repository": "Overhold"
    },
    {
        "username": "dfenech0",
        "repository": "Pannier"
    },
    {
        "username": "dfenech0",
        "repository": "Sonair"
    },
    {
        "username": "dfenech0",
        "repository": "Tampflex"
    },
    {
        "username": "dgraundisson2a",
        "repository": "Home Ing"
    },
    {
        "username": "dgraundisson2a",
        "repository": "Keylex"
    },
    {
        "username": "dpartkya14",
        "repository": "Stronghold"
    },
    {
        "username": "dterry1l",
        "repository": "Regrant"
    },
    {
        "username": "dterry1l",
        "repository": "Toughjoyfax"
    },
    {
        "username": "dterry1l",
        "repository": "Tres-Zap"
    },
    {
        "username": "dwrinchh",
        "repository": "Alphazap"
    },
    {
        "username": "dwrinchh",
        "repository": "Biodex"
    },
    {
        "username": "dwrinchh",
        "repository": "Bytecard"
    },
    {
        "username": "dwrinchh",
        "repository": "Transcof"
    },
    {
        "username": "edumini2d",
        "repository": "Bitchip"
    },
    {
        "username": "ejennings26",
        "repository": "Stim"
    },
    {
        "username": "ejennings26",
        "repository": "Y-Solowarm"
    },
    {
        "username": "eknowlson1g",
        "repository": "Latlux"
    },
    {
        "username": "eknowlson1g",
        "repository": "Ronstring"
    },
    {
        "username": "erenonu",
        "repository": "Latlux"
    },
    {
        "username": "erenonu",
        "repository": "Rank"
    },
    {
        "username": "erenonu",
        "repository": "Transcof"
    },
    {
        "username": "etampion1b",
        "repository": "Flowdesk"
    },
    {
        "username": "etampion1b",
        "repository": "Kanlam"
    },
    {
        "username": "etampion1b",
        "repository": "Konklux"
    },
    {
        "username": "eyabsley12",
        "repository": "Aerified"
    },
    {
        "username": "eyabsley12",
        "repository": "Transcof"
    },
    {
        "username": "fcastellucci1f",
        "repository": "Bytecard"
    },
    {
        "username": "fcastellucci1f",
        "repository": "Cardify"
    },
    {
        "username": "fcastellucci1f",
        "repository": "Cookley"
    },
    {
        "username": "fcastellucci1f",
        "repository": "Hatity"
    },
    {
        "username": "fcastellucci1f",
        "repository": "Kanlam"
    },
    {
        "username": "fde2e",
        "repository": "Veribet"
    },
    {
        "username": "fgollin1e",
        "repository": "Aerified"
    },
    {
        "username": "fgollin1e",
        "repository": "Namfix"
    },
    {
        "username": "fhorsell15",
        "repository": "Trippledex"
    },
    {
        "username": "fhorsell15",
        "repository": "Zoolab"
    },
    {
        "username": "frobilart23",
        "repository": "Kanlam"
    },
    {
        "username": "ftaylersong",
        "repository": "Tin"
    },
    {
        "username": "ftaylersong",
        "repository": "Viva"
    },
    {
        "username": "ggaskampl",
        "repository": "Prodder"
    },
    {
        "username": "ghamper20",
        "repository": "Zathin"
    },
    {
        "username": "ghyslop1m",
        "repository": "Bitchip"
    },
    {
        "username": "gmaccaughen1s",
        "repository": "Alphazap"
    },
    {
        "username": "gmaccaughen1s",
        "repository": "Stronghold"
    },
    {
        "username": "gmidgley1a",
        "repository": "Hatity"
    },
    {
        "username": "gmidgley1a",
        "repository": "Opela"
    },
    {
        "username": "gmidgley1a",
        "repository": "Prodder"
    },
    {
        "username": "gsedgeworth2c",
        "repository": "Andalax"
    },
    {
        "username": "gsedgeworth2c",
        "repository": "Latlux"
    },
    {
        "username": "gsedgeworth2c",
        "repository": "Temp"
    },
    {
        "username": "gsedgeworth2c",
        "repository": "Transcof"
    },
    {
        "username": "gverrechia2b",
        "repository": "Konklux"
    },
    {
        "username": "hcalveley27",
        "repository": "Bitwolf"
    },
    {
        "username": "hcalveley27",
        "repository": "Flowdesk"
    },
    {
        "username": "hcalveley27",
        "repository": "Namfix"
    },
    {
        "username": "hcalveley27",
        "repository": "Sub-Ex"
    },
    {
        "username": "hcalveley27",
        "repository": "Vagram"
    },
    {
        "username": "hvoas18",
        "repository": "Sonsing"
    },
    {
        "username": "jadamef",
        "repository": "Solarbreeze"
    },
    {
        "username": "jpaulitschkex",
        "repository": "Andalax"
    },
    {
        "username": "jpaulitschkex",
        "repository": "Mat Lam Tam"
    },
    {
        "username": "jpaulitschkex",
        "repository": "Stringtough"
    },
    {
        "username": "jpaulitschkex",
        "repository": "Trippledex"
    },
    {
        "username": "jpaulitschkex",
        "repository": "Y-Solowarm"
    },
    {
        "username": "jsokale1v",
        "repository": "Aerified"
    },
    {
        "username": "jsokale1v",
        "repository": "Flexidy"
    },
    {
        "username": "jtapper2q",
        "repository": "Voyatouch"
    },
    {
        "username": "kduckels2g",
        "repository": "Trippledex"
    },
    {
        "username": "klanchbery1q",
        "repository": "Biodex"
    },
    {
        "username": "klanchbery1q",
        "repository": "Zathin"
    },
    {
        "username": "ktidboldq",
        "repository": "Biodex"
    },
    {
        "username": "ktidboldq",
        "repository": "Flowdesk"
    },
    {
        "username": "ktidboldq",
        "repository": "Kanlam"
    },
    {
        "username": "ktidboldq",
        "repository": "Lotstring"
    },
    {
        "username": "ktidboldq",
        "repository": "Tampflex"
    },
    {
        "username": "lcutridge22",
        "repository": "Opela"
    },
    {
        "username": "ldriscoll24",
        "repository": "Alphazap"
    },
    {
        "username": "ldriscoll24",
        "repository": "It"
    },
    {
        "username": "ldriscoll24",
        "repository": "Ventosanzap"
    },
    {
        "username": "lkittle4",
        "repository": "Prodder"
    },
    {
        "username": "lkittle4",
        "repository": "Sonsing"
    },
    {
        "username": "llanbertonis",
        "repository": "Andalax"
    },
    {
        "username": "llanbertonis",
        "repository": "Prodder"
    },
    {
        "username": "lmclardie13",
        "repository": "Flowdesk"
    },
    {
        "username": "lmclardie13",
        "repository": "Matsoft"
    },
    {
        "username": "lspringaten",
        "repository": "Regrant"
    },
    {
        "username": "lspringaten",
        "repository": "Subin"
    },
    {
        "username": "lwindus2j",
        "repository": "Alphazap"
    },
    {
        "username": "lwindus2j",
        "repository": "Temp"
    },
    {
        "username": "mbezzant17",
        "repository": "Alpha"
    },
    {
        "username": "mcorriso",
        "repository": "Stringtough"
    },
    {
        "username": "mgillino25",
        "repository": "Hatity"
    },
    {
        "username": "mhendrickxc",
        "repository": "Cookley"
    },
    {
        "username": "mhendrickxc",
        "repository": "Matsoft"
    },
    {
        "username": "mlaugharne9",
        "repository": "Bigtax"
    },
    {
        "username": "mlaugharne9",
        "repository": "Tres-Zap"
    },
    {
        "username": "mlumsdend",
        "repository": "Tres-Zap"
    },
    {
        "username": "mmaccomiskey11",
        "repository": "Alphazap"
    },
    {
        "username": "mmaccomiskey11",
        "repository": "Flexidy"
    },
    {
        "username": "mmaccomiskey11",
        "repository": "Trippledex"
    },
    {
        "username": "mmelland1h",
        "repository": "Cardguard"
    },
    {
        "username": "mmelland1h",
        "repository": "Mat Lam Tam"
    },
    {
        "username": "noffai",
        "repository": "Fix San"
    },
    {
        "username": "nrehme1t",
        "repository": "Fixflex"
    },
    {
        "username": "nrehme1t",
        "repository": "Gembucket"
    },
    {
        "username": "nrehme1t",
        "repository": "Zontrax"
    },
    {
        "username": "ntandy2m",
        "repository": "Transcof"
    },
    {
        "username": "oalchinr",
        "repository": "Kanlam"
    },
    {
        "username": "orzehor1d",
        "repository": "Keylex"
    },
    {
        "username": "osavine1u",
        "repository": "Redhold"
    },
    {
        "username": "phobble10",
        "repository": "Alphazap"
    },
    {
        "username": "phobble10",
        "repository": "Zoolab"
    },
    {
        "username": "pstrood1r",
        "repository": "Fix San"
    },
    {
        "username": "rgirton2",
        "repository": "Bigtax"
    },
    {
        "username": "rgirton2",
        "repository": "Fixflex"
    },
    {
        "username": "rgirton2",
        "repository": "Konklab"
    },
    {
        "username": "rgirton2",
        "repository": "Rank"
    },
    {
        "username": "rlobe2h",
        "repository": "Fixflex"
    },
    {
        "username": "rlobe2h",
        "repository": "Overhold"
    },
    {
        "username": "schicchetto1i",
        "repository": "Gembucket"
    },
    {
        "username": "schicchetto1i",
        "repository": "Regrant"
    },
    {
        "username": "shatt2k",
        "repository": "Latlux"
    },
    {
        "username": "shatt2k",
        "repository": "Sub-Ex"
    },
    {
        "username": "sjillett1p",
        "repository": "Greenlam"
    },
    {
        "username": "sjillett1p",
        "repository": "Matsoft"
    },
    {
        "username": "sjillett1p",
        "repository": "Voltsillam"
    },
    {
        "username": "smammatt28",
        "repository": "Aerified"
    },
    {
        "username": "smammatt28",
        "repository": "Keylex"
    },
    {
        "username": "smammatt28",
        "repository": "Solarbreeze"
    },
    {
        "username": "smammatt28",
        "repository": "Temp"
    },
    {
        "username": "smammatt28",
        "repository": "Transcof"
    },
    {
        "username": "sphillips7",
        "repository": "Fix San"
    },
    {
        "username": "sphillips7",
        "repository": "Transcof"
    },
    {
        "username": "tkinsleyv",
        "repository": "Gembucket"
    },
    {
        "username": "tleadsy",
        "repository": "Duobam"
    },
    {
        "username": "tleadsy",
        "repository": "Mat Lam Tam"
    },
    {
        "username": "tpriestm",
        "repository": "Subin"
    },
    {
        "username": "umcgerraghtyz",
        "repository": "Bamity"
    },
    {
        "username": "umcgerraghtyz",
        "repository": "Opela"
    },
    {
        "username": "umcgerraghtyz",
        "repository": "Ventosanzap"
    },
    {
        "username": "wobbard19",
        "repository": "Aerified"
    },
    {
        "username": "xfaraday2i",
        "repository": "Cookley"
    },
    {
        "username": "xfaraday2i",
        "repository": "Fintone"
    },
    {
        "username": "xfaraday2i",
        "repository": "Sub-Ex"
    },
    {
        "username": "xfaraday2i",
        "repository": "Zoolab"
    }
]


def populate_server():
    container = client.containers.get(os.getenv('GITSERVER_CONTAINER'))
    for repo in repositories:
        _, stream = container.exec_run(f"mkrepo {repo['username']} {repo['repository']}", stream=True)
        for data in stream:
            print(data.decode())


if __name__ == '__main__':
    populate_server()

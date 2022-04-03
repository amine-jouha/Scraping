import urllib.request
arr= [
{"chapter": "1000", "img": "https://1.bp.blogspot.com/--vS3e_oawXQ/X-tt_jDO0vI/AAAAAAAAJlw/VLfTmJXIBpM5vshXepQCxSsOdr7BtkgtQCNcBGAsYHQ/s1600/001.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-pKxOAa452B8/X-tt_f2LAlI/AAAAAAAAJlo/GoZHHluwSVUTQtcbI4rG4rn-Meffn83EwCNcBGAsYHQ/s1600/002.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-a7LBalETW1M/X-tt_Z5l8DI/AAAAAAAAJls/ITsNeLOP6yAcPB5qFxQd-NzY5ss0DGa1gCNcBGAsYHQ/s1600/003.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-huV2_pBi-BY/X-tuALpb2QI/AAAAAAAAJl0/pZrF0xKUNYUBNFYTYW8N0usnXicTK_IwACNcBGAsYHQ/s1600/004.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-JYx1c1fkGIg/X-tuAeKfrTI/AAAAAAAAJl4/eYdQ7K_Z5voyJ-V_pLbo4_SI-_7qX1-egCNcBGAsYHQ/s1600/005.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-eVIUR4CT52w/X-tuAUWcj8I/AAAAAAAAJl8/GZpjCTIkT0MxWbC1FAZoAEk768F0x29bwCNcBGAsYHQ/s1600/006.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-4oMaDclYPNY/X-tuAqndFSI/AAAAAAAAJmA/yqea4Xtknns5LI4sKbfmsLU-4ZvL2dCnQCNcBGAsYHQ/s1600/007.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-KOgvk4bwz-4/X-tuA7GcWhI/AAAAAAAAJmE/S3t2QcRSbbU6OPG27l_Gz6mNR3AXr-b6QCNcBGAsYHQ/s1600/008.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-VEVTfj3ze1o/X-tuBBPOVBI/AAAAAAAAJmI/pZ8jq7gWW9o8GGM9vqeUuoiTmu_DJxahQCNcBGAsYHQ/s1600/009.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-06yuBz3R7K0/X-tuBOl84zI/AAAAAAAAJmM/P2yJaG0TW8MLmgEjikSq4JAuyKSrPps9QCNcBGAsYHQ/s1600/010.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-jW0D_eHN0h8/X-tuBYbj-UI/AAAAAAAAJmQ/Kq9VKc2FjNE4puGq2QJtIUFZ5GWCHzg4QCNcBGAsYHQ/s1600/011.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-vmgiELiPkdQ/X-tuBkLv2lI/AAAAAAAAJmU/jKau6jXyzrAMW9cpWr3LPbFawua-rHoBACNcBGAsYHQ/s1600/012.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-zdBvoY8dmWk/X-tuBgccXrI/AAAAAAAAJmY/1GcgQJs7_SY2IjepeLScLb8Mniu9CUJCgCNcBGAsYHQ/s1600/013.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-t7B8B1mb9sM/X-tuCHLKRLI/AAAAAAAAJmc/-xHpVhPi4kkAunx4iIhoAHasiHG0OPXGgCNcBGAsYHQ/s1600/014.jpg"},
{"chapter": "1000", "img": "https://1.bp.blogspot.com/-HLcYU62HRu4/X-tuCZJ2lYI/AAAAAAAAJmg/oX28ZqRrPXsBixLHCAT8z71fjeVr_cY8QCNcBGAsYHQ/s1600/015.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-V5b6ivMw7ks/YAL7L7Bo6dI/AAAAAAAAJnA/81vt8Yc7L9o72U_ml08wLzOX9XNePXhAACNcBGAsYHQ/s1600/001.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-gN0WRZq9iBs/YAL7Nj7Z4DI/AAAAAAAAJnE/-68IO27ZQTAd6f3aosHiZNBaySkulGR_ACNcBGAsYHQ/s1600/002.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-r8q_L703lqs/YAL7PcTLR6I/AAAAAAAAJnI/qbGL1f2oQ9cUSP0n49SOUCyX_MdbZZK0wCNcBGAsYHQ/s1600/003.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-KBANlDcWQp0/YAL7RVtXtCI/AAAAAAAAJnM/HZ-zEBkwCN0ghNEAaN71GtcFpbXPveUbQCNcBGAsYHQ/s1600/004.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-zkc7dTDpjKU/YAL7TMHeNuI/AAAAAAAAJnQ/vNexcnLYa0MLFixPDSAKGEp-Ged6kucfgCNcBGAsYHQ/s1600/005.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-8D6b3T7eP9I/YAL7VvigORI/AAAAAAAAJnU/Q8PY3QbnwbA4Ejkkh7d7MOeS9_sHHYZ8gCNcBGAsYHQ/s1600/006.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-lhCbtHENcxs/YAL7XYuNSsI/AAAAAAAAJnY/W7-2QVGU6uw4tz43PJlc9i_PYK9OnzzygCNcBGAsYHQ/s1600/007.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-uBbbZNlM35w/YAL7ZUGPYoI/AAAAAAAAJnc/D5RdD0TtDXwry1kIlJLtEF4kJ_k3pV0FgCNcBGAsYHQ/s1600/008.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-oqBs2aOx6jA/YAL7bYx53_I/AAAAAAAAJng/6N8RJFXGAM8bkILM0pouEcKEom3mgVOjwCNcBGAsYHQ/s1600/009.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-MqYdUO6GUAk/YAL7fZ7ck2I/AAAAAAAAJns/92vSuBOESOcfdfaAHpKdjsjsdqEC1OoIACNcBGAsYHQ/s1600/010.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-kzCxwKXko30/YAL7dgVfLeI/AAAAAAAAJno/5faCIu-LDJMqYDiZOEXL4Dknl2h9lOF7QCNcBGAsYHQ/s1600/011.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-oRU_dqQNUYk/YAL7iAHzqxI/AAAAAAAAJn0/jMkE0poPw18UyT6bca3IQkR9p6SEs-fOgCNcBGAsYHQ/s1600/012.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-8pEom3OYpL0/YAL7lcVKu0I/AAAAAAAAJoA/CEdaZgxKzGA0O7pNpJTWOJl_REePaPPlwCNcBGAsYHQ/s1600/013.jpg"},
{"chapter": "1001", "img": "https://1.bp.blogspot.com/-srOUKdrxFH8/YAL7otV5-ZI/AAAAAAAAJoE/xpYZKUs1Q0YrWzYSbbUbZrByRVTFr8lSACNcBGAsYHQ/s1600/014.jpg"},
]
m = 0
for i in arr:
  m+=1
  num_chapter = int(i["chapter"])
  # print(num_chapter)
  if num_chapter>1000 :
    num_chapter=1001
    m=0
  urllib.request.urlretrieve(i["img"], i["chapter"]+str([m])+".png")
"""Reproduce DGPI numbers from the three DES Karnataka district tables.
Run: python reproduce_dgpi.py  (needs pandas, numpy, scipy). Writes crosswalk.csv, indicators.csv."""
import pandas as pd, numpy as np
from scipy.stats import spearmanr
G='ka_districts-gddp-pci-2025-26.csv'; Y='ka-district-yuvanidhi-2025.csv'; M='ka-district-msme-employment-2025.csv'
rd=lambda f: pd.read_csv(f,encoding='utf-8-sig')
g,y,m=rd(G),rd(Y),rd(M)
g,y,m=g[g.District!='State'].copy(),y[y.District!='Total'].copy(),m[m.District!='TOTAL'].copy()
norm=lambda s:''.join(c for c in s.lower() if c.isalpha())
# Manual aliases (spelling variants + renamed units). Ramanagara = Bengaluru South: SAME-BOUNDARY ASSUMPTION.
ALIAS={'bagalkote':'bagalkot','bangaloreurban':'bengaluru_urban','bengaluruurban':'bengaluru_urban',
'bangalorerural':'bengaluru_rural','bengalururural':'bengaluru_rural','bangaloresouth':'ramanagara',
'chamarajanagar':'chamarajanagar','chamarajanagara':'chamarajanagar','chamarajnagar':'chamarajanagar',
'chikkaballapur':'chikkaballapur','chikkaballapura':'chikkaballapur','chikballapur':'chikkaballapur',
'dakshinakannada':'dakshina_kannada','dakshinkannada':'dakshina_kannada','davanagere':'davanagere',
'davangere':'davanagere','uttarakannada':'uttara_kannada','uttarkannad':'uttara_kannada',
'yadagiri':'yadgir','yadgir':'yadgir'}
key=lambda s: ALIAS.get(norm(s),norm(s))
for n,a in (('gddp',g),('yuva',y),('msme',m)):
    a['key']=a.District.map(key); assert a.key.is_unique and len(a)==31,(n,len(a))
cw=g[['key','District']].rename(columns={'District':'gddp_name'}).merge(
   y[['key','District']].rename(columns={'District':'yuvanidhi_name'}),on='key').merge(
   m[['key','District']].rename(columns={'District':'msme_name'}),on='key')
for c in ('yuvanidhi_name','msme_name'):
    cw[c.split('_')[0]+'_match']=np.where(cw[c].map(norm)==cw.gddp_name.map(norm),'exact-normalised','manual alias')
cw.to_csv('crosswalk.csv',index=False)
print('31 of 31 matched; match types:\n',cw.yuvanidhi_match.value_counts().to_dict(),cw.msme_match.value_counts().to_dict())
d=g.merge(y[['key','Grand Total']],on='key').merge(m[['key','Total Employed']],on='key')
d['income_lakh']=d['Per Capita Income (Rs.)']/1e5
d['implied_pop']=d['NDDP Current Prices (Rs. Cr)']*1e7/d['Per Capita Income (Rs.)']   # approximation, NOT a census count
d['dgpi_per_1000']=d['Grand Total']/d.implied_pop*1000
d['msme_jobs_per_1000']=d['Total Employed']/d.implied_pop*1000
d[['District','key','income_lakh','implied_pop','Grand Total','Total Employed','dgpi_per_1000','msme_jobs_per_1000']].sort_values('dgpi_per_1000',ascending=False).to_csv('indicators.csv',index=False)
print('implied pop (m):',round(d.implied_pop.sum()/1e6,2),'| state DGPI:',round(d['Grand Total'].sum()/d.implied_pop.sum()*1000,2))
r=spearmanr(d.income_lakh,d.dgpi_per_1000)[0]; x=d[d.key!='bengaluru_urban']
rng=np.random.default_rng(42); n=len(d)
bs=[spearmanr(*d.iloc[rng.integers(0,n,n)][['income_lakh','dgpi_per_1000']].T.values)[0] for _ in range(5000)]
print('Spearman income~DGPI:',round(r,3),'| ex Bengaluru Urban:',round(spearmanr(x.income_lakh,x.dgpi_per_1000)[0],3),'| 95% CI',np.nanpercentile(bs,[2.5,97.5]).round(2))
print('Spearman DGPI~MSME density:',round(spearmanr(d.dgpi_per_1000,d.msme_jobs_per_1000)[0],2))
print(d.sort_values('dgpi_per_1000',ascending=False)[['District','dgpi_per_1000']].head(5).round(2).to_string(index=False))

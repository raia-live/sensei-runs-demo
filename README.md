# shipkit

Parcel quotes by region. One module per region under `shipkit/regions/`, each with a rate card and a
`quote(parcel, postcode)` that returns the price in minor units.

```python
from shipkit import Parcel, quote

quote("no", Parcel(weight_g=800, length_cm=20, width_cm=15, height_cm=10), "0150")
```

- How a quote is built: `docs/RATES.md`
- Working on the code: `CONTRIBUTING.md`

# How a quote is built

Every region follows the same seven steps. The rate card (the constants at the top of the region's
module) supplies the numbers; the steps do not change from region to region.

1. **Billable weight.** The greater of the parcel's actual weight and its volumetric weight, using the
   region's `VOLUME_DIVISOR`. Use `units.billable_grams`.
2. **Started kilograms.** Weight is billed per started kilogram. Use `units.started_kg`.
3. **Freight.** `BASE` plus `PER_KG` for each billed kilogram.
4. **Remote areas.** When the postcode is in a remote area, `REMOTE_FEE` is added to the freight.
   Postcodes arrive as people typed them, so match with `zones.is_remote`, never on the raw text.
5. **Fuel.** The fuel surcharge is `FUEL_BPS` of the freight, the remote fee included.
6. **Tax.** Tax is `TAX_BPS` of the freight and the fuel surcharge together.
7. **Minor units.** The total is converted once, at the end, with `money.to_minor` (halves round up).
   Nothing is rounded before that.

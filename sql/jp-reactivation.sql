select top 50 UPPER(p.Email), p.Status, p.LoyaltyTier as CurrentLoyaltyTier, p.CountryCode, st.ClassCode,
	count(distinct bd.BookingID) as NumberOfTotalBookings, 
	AVG(bd.NTR) as AveragePurchaseValue,
	min(bd.BookingYM) as FirstPurchaseDate, max(bd.BookingYM) as LatestPurchaseDate,
	sum(cm.Deliveries) as NetEmailDeliveries, sum(cm.Opens) as TotalEmailsOpened, sum(cm.DistinctOpens) as DistinctEmailsOpened,
	sum(cm.Clicks) as TotalEmailsClicked, sum(cm.DistinctClicks) as DistinctEmailsClicked, sum(cm.Unsubs) as Unsubscribed
	from Cadence_ProfileStatus2 p
	inner join (select SubscriberID, Deliveries, Opens, DistinctOpens,Clicks, DistinctClicks, Unsubs from Cadence_Metrics) as cm 
		on cm.SubscriberID = p.SubscriberID
	left outer join RCL_BookingData bd on bd.ConsumerID = p.ConsumerID
	left outer join SubscriberStatus st on UPPER(st.Email) = UPPER(p.Email)
	group by Upper(p.Email), p.Status, p.LoyaltyTier, p.CountryCode, st.ClassCode
	order by NumberOfTotalBookings desc;
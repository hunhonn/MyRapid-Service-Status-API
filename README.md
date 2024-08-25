# MyRapid-Service-Status-API
The MyRapid service status API shows the real-time train service status and service updates operated by RapidKL.
> Inspired by the API call by MTREC. However, this API is not geolocked.

## Request
Make a GET Request to [https://rapiddisruption-1-m9526224.deta.app/](url)
> No Query String is required

## Response (In JSON):

**1) Timestamp:**
Requested Time

**2) Data**
JSON Array with 6 main Rail lines:
  - KL Monorail Line (MRL)
  - MRT Kajang Line (KGL)
  - LRT Kelana Jaya Line (KJL)
  - LRT Ampang Line (AGL)
  - LRT Sri Petaling Line (SPL)
  - MRT Putrajaya Line (PYL)

**Example Response** : '{"LineID":"PYL","Line":"MRT Putrajaya Line","Status":"Normal Service","Remarks":""}' 
LineID: ID of the route
Line: Official name of the route
Status: Current Status of the line.
Remarks: If service is either "Revised" of "Out of Service", remarks will be given.

### Rate Limit
no rate limit lol

### Local ISP and Regional Limit
no geolocation i dont care where you are from.

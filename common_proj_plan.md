## 1안

1. 프로젝트 이름 : 악성코드 대응 시스템

2. 기능 설명 : 악성코드 정보를 공유하는 외부 API들을 활용해서 데이터를 긁어오고,
			      기업담당자는 방화벽 or IDS등에 해당 시그니쳐(URL, sha256) 값을 추가하여 차단 실시
		
3. 참고한 프로젝트/웹사이트가 있다면 링크
- https://bazaar.abuse.ch/api
- https://urlhaus.abuse.ch/api/

## 2안

1. 프로젝트 이름 : 원타임 네트워크 스캔 시스템

2. 기능 설명 : DigitalOcean 클라우드 시스템을 이용해서 사용자가 도메인 or IP를 입력하면 DigitalOcean VPS가 생성되고,
               NMAP과 같은 네트워크 스캔 도구를 실행하고 결과값을 반환. 그다음 생성된 DigitalOcean VPS 삭제.
		
3. 참고한 프로젝트/웹사이트가 있다면 링크
- https://www.digitalocean.com/docs/apis-clis/
- https://developers.digitalocean.com/libraries/

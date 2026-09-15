# GIAO BÀI TẬP 01: PHẦN MỀM MÃ NGUỒN MỜ

**Thông tin sinh viên:**
* **Họ và tên:** Nguyễn Công Tình
* **Mã sinh viên:** 23T1020544
* **Lớp:** K47B
* **Kho lưu trữ (Repository):** `pmnm-hocphan`

---

# BÀI 1.1: CẤU TRÚC README.MD CỦA KHO PMNM-HOCPHAN

### 1. Giới thiệu cá nhân
* **Họ và tên:** Nguyễn Công Tình
* **Mã sinh viên:** 23T1020544
* **Lớp:** K47B

---

### 2. Vì sao tôi muốn học về phần mềm mã nguồn mở?

Trong quá trình học ngành Công nghệ Thông tin, tôi nhận ra phần lớn các công cụ mà mình tiếp xúc hàng ngày — từ hệ điều hành, công cụ lập trình cho đến các thư viện xử lý — đều được phát triển trên nền tảng mã nguồn mở. Tôi chọn học học phần này với mong muốn không chỉ dừng lại ở việc sử dụng miễn phí một cách thụ động, mà hiểu sâu hơn về cơ chế vận hành, quản lý và hợp tác trong các dự án công nghệ lớn. Việc nắm vững các loại giấy phép (license) cũng rất thiết thực, giúp tôi tránh các rủi ro pháp lý hay vi phạm bản quyền khi phát triển sản phẩm sau này. Bên cạnh đó, môn học là cơ hội tốt để tôi rèn luyện quy trình làm việc chuẩn chỉnh với Git/GitHub và tự tin đóng góp (contribute) những dòng code đầu tiên cho cộng đồng.

---

### 3. Danh sách 5 phần mềm mã nguồn mở đang sử dụng hàng ngày

1. **Visual Studio Code (VS Code)**
   * **Mục đích sử dụng:** Trình chỉnh sửa mã nguồn chính cho các bài tập lập trình hàng ngày.
   * **Giấy phép:** Giấy phép MIT (áp dụng cho phần mã nguồn cốt lõi `vscode`).

2. **Linux (Ubuntu)**
   * **Mục đích sử dụng:** Hệ điều hành dùng để học tập, thực hành dòng lệnh và khởi tạo môi trường lập trình.
   * **Giấy phép:** GNU General Public License v2.0 (GPLv2).

3. **Git**
   * **Mục đích sử dụng:** Quản lý các phiên bản mã nguồn và đồng bộ hóa dự án cá nhân lên GitHub.
   * **Giấy phép:** GNU General Public License v2.0 (GPLv2).

4. **VLC Media Player**
   * **Mục đích sử dụng:** Trình phát video, nghe nhạc đa định dạng nhẹ và không chứa quảng cáo.
   * **Giấy phép:** GNU Lesser General Public License v2.1 (LGPLv2.1).

5. **Brave Browser**
   * **Mục đích sử dụng:** Trình duyệt web sử dụng hàng ngày giúp tối ưu tốc độ và tự động chặn quảng cáo.
   * **Giấy phép:** Mozilla Public License v2.0 (MPL 2.0).

---

# BÀI 1.2: PHÂN TÍCH RẼ NHÁNH DỰ ÁN MÃ NGUỒN MỜ DOH MÂU THUẪN CỘNG ĐỒNG — MYSQL VÀ MARIADB

### 1. Bối cảnh dự án gốc
MySQL được khởi xướng phát triển từ giữa những năm 1990 bởi Michael "Monty" Widenius và công ty MySQL AB. Nhờ ưu điểm nhẹ, tốc độ xử lý nhanh và hoàn toàn miễn phí, MySQL nhanh chóng trở thành hệ quản trị cơ sở dữ liệu quan hệ mã nguồn mở phổ biến nhất thế giới, trở thành xương sống cho hàng triệu trang web. Năm 2008, Sun Microsystems mua lại MySQL AB với giá 1 tỷ USD. Bước ngoặt lớn xảy ra vào năm 2009 khi tập đoàn Oracle thông báo mua lại Sun Microsystems, từ đó chính thức nắm quyền kiểm soát MySQL.

### 2. Nguyên nhân mâu thuẫn và quyết định rẽ nhánh (Fork)
Oracle vốn nổi tiếng với mô hình kinh doanh phần mềm thương mại độc quyền và chính sách cứng rắn. Sự kiện một tập đoàn thương mại lớn sở hữu dự án mã nguồn mở cốt lõi đã dấy lên mối lo ngại sâu sắc trong cộng đồng phát triển. Nhiều nhà quản trị e ngại Oracle sẽ cố tình làm suy yếu hoặc hạn chế sự phát triển của MySQL để bảo vệ sản phẩm cơ sở dữ liệu thương mại mang lại lợi nhuận cao của họ (Oracle Database).

Nhận thấy rủi ro này đối với tính tự do của phần mềm, Michael Widenius cùng các kỹ sư cốt lõi đã rời khỏi dự án và quyết định rẽ nhánh (fork) mã nguồn MySQL vào năm 2009 để tạo ra **MariaDB**. Mục tiêu chính của MariaDB là duy trì một bản sao hoàn toàn tương thích (drop-in replacement) với MySQL nhưng cam kết giữ mã nguồn mở vĩnh viễn dưới giấy phép GPL.

### 3. Diễn biến và tác động đến hệ sinh thái
Sự xuất hiện của MariaDB đã tạo nên một làn sóng dịch chuyển mạnh mẽ trong ngành công nghệ:
* **Tính mở và tốc độ cải tiến:** Trong khi bản MySQL do Oracle quản lý bị phàn nàn là phát triển khép kín và chậm trễ sửa lỗi cho cộng đồng, MariaDB lại liên tục đón nhận đóng góp, tích hợp nhiều bộ lưu trữ cơ sở dữ liệu mới (như Aria, ColumnStore) và tối ưu hiệu năng.
* **Sự chuyển dịch của các hệ điều hành:** Hàng loạt phân phối Linux lớn như Red Hat Enterprise Linux, Debian, Fedora và Arch Linux đã quyết định loại bỏ MySQL và chọn MariaDB làm hệ quản trị cơ sở dữ liệu mặc định.
* **Sự hưởng ứng từ doanh nghiệp:** Nhiều nền tảng quy mô toàn cầu như Wikipedia, Google hay Booking.com cũng chuyển hướng sử dụng MariaDB để đảm bảo tính an toàn và chủ động về mặt công nghệ.

### 4. Tình trạng hiện tại và bài học kinh nghiệm
Hiện nay, cả hai dự án vẫn song song tồn tại và phát triển theo hai hướng riêng biệt: MySQL thuộc Oracle tập trung vào nhóm khách hàng doanh nghiệp tích hợp hệ sinh thái Cloud, trong khi MariaDB trở thành sự lựa chọn ưu tiên của cộng đồng tự do.

Sự kiện rẽ nhánh giữa MySQL và MariaDB để lại một bài học đắt giá: **Giá trị cốt lõi của phần mềm mã nguồn mở nằm ở cộng đồng và giấy phép tự do**. Khi quyền lợi cộng đồng bị đe dọa bởi lợi ích doanh nghiệp, cơ chế rẽ nhánh (fork) chính là "van an toàn" giúp bảo vệ và duy trì sự sống cho sản phẩm công nghệ.

---

# BÀI 1.3: KHÁI NIỆM TRAGEDY OF THE COMMONS TRONG MÃ NGUỒN MỜ — TRƯỜNG HỢP CORE-JS

### 1. Khái niệm Tragedy of the Commons trong mã nguồn mở
"Bi kịch của mảnh đất công" (Tragedy of the Commons) là hiện tượng kinh tế học xuất hiện khi một tài nguyên chung miễn phí bị tất cả mọi người khai thác tối đa, nhưng không ai chịu bỏ chi phí hay công sức để bảo tồn, dẫn đến việc tài nguyên đó bị suy kiệt.

Trong bối cảnh phần mềm mã nguồn mở, hiện tượng này diễn ra phổ biến dưới dạng: hàng triệu công ty, tập đoàn công nghệ sử dụng các thư viện hạ tầng mã nguồn mở miễn phí để xây dựng sản phẩm thương mại thu lời hàng tỷ USD, nhưng lại không tài trợ hay hỗ trợ gì cho các nhà phát triển (maintainer) — những người đang thầm lặng duy trì hệ thống đó.

### 2. Phân tích trường hợp cụ thể: `core-js`
`core-js` là một thư viện JavaScript chịu trách nhiệm cung cấp polyfill (mã hỗ trợ các tính năng JavaScript mới chạy được trên trình duyệt cũ). Hầu như toàn bộ hệ sinh thái web hiện đại (thông qua Babel, Webpack, Create React App...) đều phụ thuộc vào `core-js`. Thư viện này đạt hàng chục đến hàng trăm triệu lượt tải về mỗi tuần.

* **Thực trạng tài chính bất hợp lý:** Mặc dù đóng vai trò là hạ tầng cho cả ngành công nghiệp web, `core-js` lại do duy nhất một nhà phát triển — Denis Pushkarev (zloirock) — gánh vác và duy trì trong nhiều năm. Denis dành toàn bộ thời gian làm việc cho dự án, nhưng số tiền quyên góp nhận được mỗi tháng chỉ vỏn vẹn vài trăm USD, không đủ chi trả sinh hoạt phí cơ bản.
* **Hậu quả bi kịch:** Khi gặp khủng hoảng tài chính và biến cố cá nhân, tác giả đã phải đưa ra những lời kêu cứu gay gắt ngay trên terminal khi người dùng cài đặt gói phần mềm. Sự kiệt sức của maintainer đe dọa trực tiếp đến sự an toàn và khả năng nâng cấp của hàng triệu ứng dụng web trên toàn thế giới.

### 3. Đề xuất cơ chế khắc phục
Để giải quyết bài toán bù đắp chi phí và giúp hệ sinh thái phát triển bền vững, cần triển khai các giải pháp thực tế sau:

* **Trích quỹ tự động từ trình quản lý gói (Package Manager Funding):** Các công ty quản lý như npm/GitHub cần xây dựng mô hình thu phí trả góp đối với các tài khoản doanh nghiệp. Một phần kinh phí này sẽ tự động phân bổ cho các maintainer dựa trên tần suất dự án của họ được các doanh nghiệp đó sử dụng.
* **Chuyển đổi sang giấy phép kép (Dual-Licensing):** Áp dụng giấy phép thương mại cho các tập đoàn có doanh thu lớn (ví dụ: bắt buộc trả phí nếu doanh thu công ty vượt 1 triệu USD/năm) và giữ giấy phép miễn phí cho cá nhân, học sinh, sinh viên hoặc tổ chức phi lợi nhuận.
* **Trách nhiệm xã hội của doanh nghiệp (OSPO - Open Source Program Office):** Các tập đoàn lớn cần thành lập bộ phận quản lý mã nguồn mở và quy định sẵn một khoản ngân sách cố định hàng năm để tài trợ trực tiếp cho các dự án hạ tầng mà họ đang phụ thuộc thông qua các nền tảng như Open Collective hay GitHub Sponsors.


## Giấy phép

Mã nguồn trong kho này được phát hành theo [Giấy phép MIT](LICENSE).

SPDX-License-Identifier: MIT

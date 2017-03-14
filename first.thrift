
namespace php langzi
struct Member {
    1: i64 id,
    2: string name,
    3: string password,
    4: string address
}

service upName{
    string EditName(1: i64 id,2: string name);
}
service upAddress{
    string EditAddress(1: i64 id,2: string address);
}
service upPwd{
    string EditPassword(1: i64 id,2: string password);
}

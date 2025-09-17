import subprocess
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# うまく切り替えられない場合はGUIDが違うのがほとんどなので、powercfg -Lとcmdで入力して以下を合わせてください。
BALANCE_GUID = "381b4222-f694-41f0-9685-ff5bb260df2e"   # バランス
ULTI_GUID    = "48db009c-83c5-4ef9-9a97-3c02ab275c4c"   # 究極のパフォーマンス
HIGH_GUID    = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"   # 高パフォーマンス
POWER_GUID   = "a1841308-3541-4fab-bc81-f71556f20b4a"   # 省電力

GUIDS = {
    BALANCE_GUID: ("バランス", (0, 120, 255)),         # 青
    POWER_GUID: ("省電力", (0, 200, 0)),              # 緑
    HIGH_GUID: ("高パフォーマンス", (200, 0, 0)),     # 赤
    ULTI_GUID: ("究極のパフォーマンス", (160, 0, 160)), # 紫
}

def get_current_scheme():
    try:
        result = subprocess.run(["powercfg", "/GETACTIVESCHEME"], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        for guid in GUIDS:
            if guid.lower() in output.lower():
                return guid
    except Exception as e:
        print("現在のプラン取得失敗:", e)
    return BALANCE_GUID

def set_scheme(icon, guid):
    try:
        subprocess.run(["powercfg", "/S", guid], check=True)
        name, color = GUIDS[guid]
        print(f"✅ {name} に切替完了")
        icon.icon = create_image(color)
    except Exception as e:
        print(f"切替失敗 ({guid}):", e)

def create_image(color=(0, 120, 255)):
    img = Image.new('RGB', (64, 64), (0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((16, 16, 48, 48), fill=color)
    return img

def make_callback(guid):
    def callback(icon, item):
        set_scheme(icon, guid)
    return callback

def main():
    menu_items = []
    for guid, (name, color) in GUIDS.items():
        menu_items.append(MenuItem(name, make_callback(guid)))
    menu_items.append(MenuItem("終了", lambda icon, item: icon.stop()))

    current_guid = get_current_scheme()
    _, color = GUIDS.get(current_guid, ("バランス", (0, 120, 255)))

    icon = Icon("PowerPlanSwitcher", create_image(color), menu=Menu(*menu_items))
    icon.run()

if __name__ == "__main__":
    main()

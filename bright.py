from PIL import Image, ImageEnhance
import os
from glob import glob

def change_brightness(input_path, output_path, brightness_factor):
    try:
        # 画像を開く
        img = Image.open(input_path)

        # 明るさを変更
        enhancer = ImageEnhance.Brightness(img)
        img_bright = enhancer.enhance(brightness_factor)

        # 新しい画像を保存
        img_bright.save(output_path)

        print(f"明るさを変更しました: {output_path}")

    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    root_input_path = r"E:\split"
    root_output_path = r"E:\gladpillow"
    dir = r"0-100"
    # 明るさの変更係数（1.0が元の明るさ）
    brightness_factor = 2  # 2倍に変更する例
    data_type = ["test","train","val"]

    if not os.path.exists(root_input_path):
        os.makedirs(root_input_path)


    for word in sorted(os.listdir(os.path.join(root_input_path,dir))):
        #print(len(os.listdir(os.path.join(args.test_dir,word))))
        word_dir = os.path.join(root_input_path,dir,word)
        #print(word_dir)

        if not os.path.exists(os.path.join(root_output_path,dir,word)):
            os.makedirs(os.path.join(root_output_path,dir,word))


        for dt in data_type:

            dt_dir = os.path.join(word_dir,dt)
            #print(dt_dir)
            if not os.path.exists(os.path.join(root_output_path,dir,word,dt)):
                os.makedirs(os.path.join(root_output_path,dir,word,dt))

            for frame in sorted(os.listdir(dt_dir)):
                frame_dir = os.path.join(dt_dir,frame)
                #print(frame_dir)
                if not os.path.exists(os.path.join(root_output_path,dir,word,dt,frame)):
                    os.makedirs(os.path.join(root_output_path,dir,word,dt,frame))

                test_low_data_name = glob(frame_dir + '\*.*')
                #print(f"testdir:{test_low_data_name}")
                #save_dir = os.path.join(root_output_path,word,dt,frame)
                for idx in range(len(test_low_data_name)):
                    #print(os.path.join("E:\split",*(test_low_data_name[idx].split("\\")[2:])))
                    if not os.path.exists(os.path.join(root_output_path,*(test_low_data_name[idx].split("\\")[2:]))):
                        #print(*(test_low_data_name[idx].split("\\")[2:]))
                        #print(os.path.join(root_output_path,*(test_low_data_name[idx].split("\\")[2:])))
                        input_image_path = os.path.join(root_input_path,*(test_low_data_name[idx].split("\\")[2:]))
                        output_image_path = os.path.join(root_output_path,*(test_low_data_name[idx].split("\\")[2:]))
                        # 明るさを変更して保存
                        change_brightness(input_image_path, output_image_path, brightness_factor)

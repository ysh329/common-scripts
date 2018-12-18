#include <opencv2/opencv.hpp>  
using namespace cv;  
using namespace std;  
  
int main()  
{  
    VideoCapture capture(0);  

    capture.set(CV_CAP_PROP_FRAME_WIDTH, 640);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT, 480);  
    while (true)  
    {  
        Mat frame;  
        capture >> frame;  
        imshow("camera", frame);  
        waitKey(30);    //延时30  
    }  
    return 0; 
} 
